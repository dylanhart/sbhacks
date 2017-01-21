import os

from .settings import *

DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
STATIC_ROOT = os.path.join(BASE_DIR, "static")
