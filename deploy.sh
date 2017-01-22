#!/usr/bin/env bash

pkill gunicorn
python3 manage.py migrate --settings sbhacks.server_settings
python3 manage.py collectstatic --settings sbhacks.server_settings
gunicorn sbhacks.wsgi -D
