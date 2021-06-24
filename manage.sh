#!/bin/zsh
PROJECT_DIR="" # variable for scripts
SUB_REPO="nuxt-black-dashboard" # unmodifiable git sub repo
FRONTEND_APP="frontend" # frontend app dir
BACKEND_APP='backend' # backend app dir
EXCLUDE=("pages" "layout" "components/UserProfile") # excluded dirs of SUB_REPO

_m() { # colored message function, using variants: _m $code $message | _m $message | $code. Codes: 0=err, 1=success
  if [ "$1" = 0 ]; then
    [[ -z "$2" ]] && echo "\e[91mSomething went wrong ¯\_(ツ)_/¯\e[0m" || echo -"$3" "\e[91m$2\e[0m"
  elif [ "$1" = 1 ]; then
    [[ -z "$2" ]] && echo "\e[92mTask completed\e[0m" || echo -"$3" "\e[92m$2\e[0m"
  elif [ "$1" != 0 ] && [ "$1" != 1 ]; then echo -"$2" "\e[94m$1\e[0m"; fi
}

_e() { # sets and get environment, get or g, _e DEBUG True .env or _e g DEBUG .env > True
  if [[ $1 == "get" ]] || [[ $1 == "g" ]]; then
    val=$(sed -n "/${2}/p" .env | sed 's/.*=//')
    echo $val
  else
    sed -i.bu "s/${1}=.*/${1}=${2}/" "$3";[[ ! "$4" == "m" ]] && _m "The set variable ${1} is ${2}"
  fi
}

# shellcheck disable=SC2120
postgres() {
  : run dev database container, additional args - stop/specify env file
  env=".env"
  if [ "$1" = "stop" ]; then
    docker stop "$SQL_DATABASE" | _m "${SQL_DATABASE} down";return
  else;env="$1";fi
  if [[ ! -f $env ]];then _m 0 "${env} is not set!";return;fi

    for var in "SQL_DATABASE" "SQL_USER" "SQL_PASSWORD" "SQL_PORT"; do
        res=$(_e g "${var}" $env)
        eval "${var}=$res"
  done
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
  : frontend pre-commit script, retrieve changes from sub module
  cd "${PROJECT_DIR}/${FRONTEND_APP}/${SUB_REPO}" || return
  _m "Copying the modified and untracked files from the submodule"
  rsync -R $(git ls-files . -mo --full-name | egrep -v "node_modules" | egrep -v ".nuxt") ../
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
      if [[ -z $(ls | egrep -v $SUB_REPO ) ]]; then _m 0 "the ${FRONTEND_APP} is empty, it is probably already deployed";return;fi
      _m "Cleaning excluded dir"
      for val in $EXCLUDE; do
        rm -rf $SUB_REPO/$val
      done
      rsync -R $(git ls-files . | egrep -v $SUB_REPO) $SUB_REPO/
      vared -p "Do you want to install node packages? Default y/n: " -c npm
      case "$npm" in y | Y) npm install;;
                       n | N) _m "You need use './manage.sh -f install' for install node packages";;
                       *);;
      esac
      rm -rf $(ls | egrep -v $SUB_REPO)
      _m 1;;
  b | backend)
    vared -p 'What would you like to do?([p]ostgres/[s]qlite): ' -c db
    env=".env";if [ ! -f .env ]; then cp .env.template .env;fi
    case "$db" in p | postgres)
      _e SQL_ENGINE django.db.backends.postgresql_psycopg2 $env
      _e SQL_DATABASE backend $env
      _e SQL_USER postgres $env
      _e SQL_PASSWORD 123 $env
      _e SQL_HOST 0.0.0.0 $env
      _e SQL_PORT 5432 $env
      _e DJANGO_SECRET_KEY $(cat /dev/urandom | env LC_CTYPE=C tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1) $env
      _e DEBUG True $env
      postgres
      ;;s | sqlite)
      _e SQL_ENGINE django.db.backends.sqlite3 $env
      _e SQL_DATABASE db.sqlite3 $env
      _e DJANGO_SECRET_KEY $(cat /dev/urandom | env LC_CTYPE=C tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1) $env
      _e DEBUG True $env
      ;;*) echo "DB isn't selected";return;;
    esac
    sleep 5
    rm .env.bu
    -b makemigrations
    -b migrate
      ;; *) echo "DB isn't selected";return;;
esac
}

-b() {
  : Running backend cli commands, use add for install package
  if [[ $1 = "add" ]]; then
      poetry add "${@:2}"
  else
    python manage.py "$@"
  fi
}

-f() {
  : Manage package.json scripts, use add for install package
  if [[ $1 = "add" ]];
    npm install "${@:2}"
  cd "${PROJECT_DIR}/${FRONTEND_APP}/${SUB_REPO}" || return
  npm run "$@"
}

if [ -z "$1" ]; then # If there are no arguments, displays a list of functions and their description
  _m "Available functions: "
  echo "\e[36m"
  typeset -f | grep -w '()' -A1 | grep -v "^--" | sed 's/[(){}]//g' |
    sed 's/[[:space:]]*:[[:space:]]*/:/g' | sed 'N;s/\n/ /' | awk '!/help|_/ {print $0}'
  echo "\e[0m"
  exit 0
fi

export PROJECT_DIR=$PWD
"$@"
