#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z postgres 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

echo "migration start"
flask db init
flask db migrate
flask db upgrade
echo "migration end"

gunicorn -b 0.0.0.0:5000 manage:app --reload --log-level debug