#!/bin/zsh

SUB_REPO="nuxt-black-dashboard"
FRONTEND_APP="frontend"
PROJECT_DIR=""
BACKEND_APP='backend'
DB_CONTAINER="${BACKEND_APP}_postgres"
DB_NAME=$BACKEND_APP
DB_USER="postgres"
DB_PASSWORD="123"

_m (){ # colored message function, using variants: _m $code $message | _m $message | $code. Codes: 0=err, 1=success
  if [ "$1" = 0 ];then [[ -z "$2" ]]&&echo "\e[31mSomething went wrong ¯\_(ツ)_/¯\e[0m"||echo "\e[31m$2\e[0m"
  elif [ "$1" = 1 ];then [[ -z "$2" ]]&&echo "\e[32mTask completed\e[0m"||echo "\e[32m$2\e[0m"
  elif [ "$1" != 0 ] && [ "$1" != 1 ];then echo "\e[36m$1\e[0m";fi
}

postgres (){
    : run dev database container, access with
    if [ "$1" = "stop" ]; then
        # shellcheck disable=SC2216
        # shellcheck disable=SC2016
        docker stop "$DB_DB_CONTAINER" | _m "${DB_CONTAINER} down"
        return
    fi
    # shellcheck disable=SC2086
    docker stop $DB || true
    if [[ $# -le 3 ]];then
        _m 0 "Arguments required: name, user, password, db_name"
    exit 2
    else
        _m "Trying start container..."
    fi
    response=$(docker run --rm --detach --name=$DB_CONTAINER \
        --env POSTGRES_USER=$DB_USER \
        --env POSTGRES_PASSWORD=$DB_PASSWORD \
        --env POSTGRES_DB=$DB_NAME\
        --publish 5432:5432 postgres>/dev/null)
    [[ -z $response ]] || exit 2
}

fprecommit () {
  : pre-commit
  # shellcheck disable=SC2164
  cd "$PROJECT_DIR"/$FRONTEND_APP/$SUB_REPO
  # shellcheck disable=SC2046
  _m "Copying the modified and untracked files from the submodule"
  # shellcheck disable=SC2046
  rsync -R $(git ls-files . -mo --full-name) ../
  git reset --hard HEAD
  _m "Submodule reset"
  # shellcheck disable=SC2103
  cd ..
  # shellcheck disable=SC2035
  git add *
  _m 1
}

deploy () {
  : deploy project for work, keys: frontend, backend
  # shellcheck disable=SC2164
  if [ -z $BACKEND_APP ] || [ -z $FRONTEND_APP ];then
      _err "BACKEND_APP or FRONTEND_APP is not set!"
      exit 2
  fi
  # shellcheck disable=SC2164

  if [ "$1" = "frontend" ]; then
      _m "Copying current working files to submodule directory"
      # shellcheck disable=SC2164
      cd "$PROJECT_DIR"/$FRONTEND_APP
      # shellcheck disable=SC2046
      # shellcheck disable=SC2196
      rsync -R $(git ls-files . | egrep -v $SUB_REPO) $SUB_REPO/
      # shellcheck disable=SC2046
      # shellcheck disable=SC2196
      # shellcheck disable=SC2012
      rm -rf $(ls | egrep -v $SUB_REPO)
      _m 1

  elif [ "$1" = "backend" ]; then
      python manage.py makemigrations
      python manage.py migrate
      if [ ! -f .env ];then
        cp .env.template .env
        _m 0 ".env needs to be configured"
      fi
  else
        _m 0 "Parameter not specified"
  fi
}

-x (){
    : Running backend cli commands
    # shellcheck disable=SC2068
    python manage.py $@
}

if [ -z "$1" ]; then # prints public command description, if this file called without args
    echo "\e[36m";typeset -f | grep -w '()' -A1 | grep -v "^--" | sed 's/[(){}]//g' |
    sed 's/[[:space:]]*:[[:space:]]*/:/g' | sed 'N;s/\n/ /' | awk '!/help|_/ {print $0}';echo "\e[0m"
    exit 0
fi

export PROJECT_DIR=$PWD
"$@"