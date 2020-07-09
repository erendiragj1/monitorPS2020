#!/bin/sh

sleep 15

python3 -u manage.py makemigrations
python3 -u manage.py migrate
#python3 -u /codigo/manage.py runserver 0.0.0.0:8000
gunicorn --bind :8000 MonitorServers.wsgi:application --reload
