#!/usr/bin/env bash

pkill gunicorn
python3 manage.py migrate --settings sbhacks.server_settings --no-input
python3 manage.py collectstatic --settings sbhacks.server_settings --no-input
gunicorn sbhacks.wsgi -D
