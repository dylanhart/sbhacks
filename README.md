
# Fake News Detector Web

## To Deploy

1. `git remote add server git@the-server:sbhacks`
1. `git push server master`
1. `ssh root@the-server`
1. `cd /opt/sbhacks`
1. kill gunicorn
1. `git pull`
1. `python3 manage.py collectstatic`
1. `gunicorn sbhacks.wsgi -D`
