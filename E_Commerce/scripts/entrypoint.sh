#!/bin/sh
echo "Waiting for postgres to be ready..."
while ! nc -z db 5432; do
    sleep 1
done
python manage.py migrate
echo "Postgres is ready, starting the application..."
exec "$@"     