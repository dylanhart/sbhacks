#!/usr/bin/env bash

pkill gunicorn
python3 manage.py migrate --settings sbhacks.sever_settings
python3 manage.py collectstatic --settings sbhacks.sever_settings
gunicorn sbhacks.wsgi -D
