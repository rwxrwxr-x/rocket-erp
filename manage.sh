#!/bin/zsh

SUB_REPO="nuxt-black-dashboard"
FRONTEND_APP="frontend"
PROJECT_DIR=""
BACKEND_APP='backend'
DB_CONTAINER='{BACKEND_APP}_postgres'
DB_NAME='{BACKEND_APP}'
DB_USER="postgres"
DB_PASSWORD="123"


postgres (){
    : run dev database container, access with
    if [ "$1" = "stop" ]; then
        # shellcheck disable=SC2216
        docker stop "$DB" | echo '$DB stopped'
        return
    fi
    # shellcheck disable=SC2086
    docker stop $DB || true
    if [[ $# -le 3 ]];then
        echo "Arguments required: name, user, password, db_name"
    exit 2
    else
        echo "Try start container..."
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
  ls
  # shellcheck disable=SC2046
  rsync -R $(git ls-files . -mo --full-name) ../
  get reset --hard HEAD
  cd
}

deploy () {
  : deploy project for work, keys: frontend, backend
  # shellcheck disable=SC2164
  if [ -z $BACKEND_APP ] || [ -z $FRONTEND_APP ];then
      echo "FUCK"
      return
  fi
  # shellcheck disable=SC2164

  if [ "$1" = "frontend" ]; then
      # shellcheck disable=SC2164
      cd "$PROJECT_DIR"/$FRONTEND_APP
      rsync -R / $SUB_REPO
      # shellcheck disable=SC2046
      # shellcheck disable=SC2196
      # shellcheck disable=SC2012
      rm -rf $(ls | egrep -v $SUB_REPO)

  elif [ "$1" = "backend" ]; then
      python manage.py makemigrations
      python manage.py migrate
      cp .env.template .env
      echo ".env needs to be configured !"
  fi
}

-x (){
    : Running backend cli commands
    # shellcheck disable=SC2068
    python manage.py $@
}

if [ -z $1 ]; then
    typeset -f | grep -w '()' -A1 | grep -v "^--" |
    sed 's/[(){}]//g' | sed 's/[[:space:]]*:[[:space:]]*/:/g' |
    sed 'N;s/\n/ /' | awk '!/help|_/ {print $0}'
    exit 0
fi


export PROJECT_DIR=$PWD
poetry shell
"$@"