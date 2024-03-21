#!/bin/bash

if [ "$DB_NAME" = "elanelweb" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Ejecutar los comandos que deseas realizar después de que PostgreSQL esté disponible
python manage.py migrate --no-input
python manage.py collectstatic --no-input --clear

# Iniciar el servidor Django
exec "$@"