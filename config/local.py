from .base import *

DEBUG = True

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "you will never guess")

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("DB_NAME"),
        'USER': os.environ.get("DB_USER"),
        'PASSWORD': os.environ.get("DB_PASSWORD"),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
