#!/bin/sh

# Script that ensures postgres is up and running
# and healthy before communicating with it

echo "Waiting for postgres....."

while ! nc -z web-db 5432; do
    sleep 0.1
done

echo "PostgreSQL started"

exec "$@"