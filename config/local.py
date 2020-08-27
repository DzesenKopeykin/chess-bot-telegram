from .base import *

DEBUG = True

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "you will never guess")

ALLOWED_HOSTS = ["*"]
