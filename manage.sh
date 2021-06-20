#!/bin/zsh
PROJECT_DIR=""
SUB_REPO="nuxt-black-dashboard"
FRONTEND_APP="frontend"
BACKEND_APP='backend'

_m() { # colored message function, using variants: _m $code $message | _m $message | $code. Codes: 0=err, 1=success
  if [ "$1" = 0 ]; then
    [[ -z "$2" ]] && echo "\e[91mSomething went wrong ¯\_(ツ)_/¯\e[0m" || echo -"$3" "\e[91m$2\e[0m"
  elif [ "$1" = 1 ]; then
    [[ -z "$2" ]] && echo "\e[92mTask completed\e[0m" || echo -"$3" "\e[92m$2\e[0m"
  elif [ "$1" != 0 ] && [ "$1" != 1 ]; then echo -"$2" "\e[94m$1\e[0m"; fi
}

_env() { # sets and get environment
  if [[ $1 == "get" ]]; then
    source "$2"
  else
    sed -i.bu "s/${1}=.*/${1}=${2}/" "$3";[[ ! "$4" == "m" ]] && _m "The set variable ${1} is ${2}"
  fi
}
# shellcheck disable=SC2120
postgres() {
  : run dev database container, access with
  if [ "$1" = "stop" ]; then
    docker stop "$SQL_DATABASE" | _m "${SQL_DATABASE} down"
    return
  fi
  [[ ! -f .env ]] && return;_env get .env
  # shellcheck disable=SC2143
  [[ -n $(docker ps -f name="$SQL_DATABASE" | grep -w "$SQL_DATABASE") ]] && docker stop "$SQL_DATABASE" | _m "${SQL_DATABASE} down"
  _m "Trying to start container..."
  response=$(docker run --rm --detach --name="$SQL_DATABASE" \
    --env POSTGRES_USER="$SQL_USER" \
    --env POSTGRES_PASSWORD="$SQL_PASSWORD" \
    --env POSTGRES_DB="$SQL_DATABASE" \
    --publish "$SQL_PORT":5432 postgres >/dev/null)
  [[ -z $response ]] && _m 1 "${SQL_DATABASE} container is started." || exit 2
}

pre-commit() {
  : pre-commit
  cd "${PROJECT_DIR}/${FRONTEND_APP}/${SUB_REPO}" || return
  _m "Copying the modified and untracked files from the submodule"
  rsync -R "$(git ls-files . -mo --full-name)" ../
  git reset --hard HEAD
  _m "Submodule reset"
  cd ..
  git add ./*
  _m 1
}
deploy() {
  : deploy project for work, dialogue
  if [ -z "$BACKEND_APP" ] || [ -z "$FRONTEND_APP" ]; then
    _err "BACKEND_APP or FRONTEND_APP is not set!"
    exit 2
  fi

  vared -p "What would you like to do? [f]frontend, [b]ackend: " -c state
  case "$state" in
  f | frontend)
      _m "Copying current working files to submodule directory"
      cd "${PROJECT_DIR}/${FRONTEND_APP}" || return
      if [[ -n $(ls | egrep -v $SUB_REPO ) ]]; then _m 0 "the ${FRONTEND_APP} is empty, it is probably already deployed";return;fi
      rsync -R $(git ls-files . | egrep -v $SUB_REPO) $SUB_REPO/
      vared -p "Do you want to install node packages? Default y/n: " -c npm
      case "$state" in y | Y) npm install;;
                       n | N) return;;
                       *) npm install;;
      esac
      rm -rf "$(ls | egrep -v $SUB_REPO)"
      _m 1;;
  b | backend)
    vared -p 'What would you like to do?([p]ostgres/[s]qlite): ' -c db
    env=".env";if [ ! -f .env ]; then cp .env.template .env;fi
    case "$db" in p | postgres)
      _env SQL_ENGINE django.db.backends.postgresql_psycopg2 $env
      _env SQL_DATABASE backend $env
      _env SQL_USER postgres $env
      _env SQL_PASSWORD 123 $env
      _env SQL_HOST 0.0.0.0 $env
      _env SQL_PORT 5432 $env
      _env DJANGO_SECRET_KEY "$(shuf -zer -n20 {A..Z}{a..z}{0..9})" $env
      _env DEBUG True $env
      postgres
      ;;s | sqlite)
      _env SQL_ENGINE django.db.backends.sqlite3 $env
      _env SQL_DATABASE db.sqlite3 $env
      _env SQL_USER " " $env
      _env SQL_PASSWORD " " $env
      _env SQL_HOST " " $env
      _env SQL_PORT " " $env
      _env DJANGO_SECRET_KEY 123 $env
      _env DEBUG True $env
      ;;*) echo "DB isn't selected";return;;
    esac
    sleep 5
    -b makemigrations
    -b migrate
      ;; *) echo "DB isn't selected";return;;
esac
}

-b() {
  : Running backend cli commands
  python manage.py "$@"
}

-f() {
  : Manage package.json scripts
  cd "${PROJECT_DIR}/${FRONTEND_APP}/${SUB_REPO}" || return
  npm run "$@"
}

if [ -z "$1" ]; then # prints public command description, if this file called without args
  echo "\e[36m"
  typeset -f | grep -w '()' -A1 | grep -v "^--" | sed 's/[(){}]//g' |
    sed 's/[[:space:]]*:[[:space:]]*/:/g' | sed 'N;s/\n/ /' | awk '!/help|_/ {print $0}'
  echo "\e[0m"
  exit 0
fi

export PROJECT_DIR=$PWD
"$@"
