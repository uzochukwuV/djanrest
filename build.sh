#!/bin/bash

# build

echo "build"
python -m pip install requirements.txt

echo "migrating"
python manage.py makemigrations
python manage.py migrate

echo "collecting static"
python manage.py collectstatic --noinput --clear