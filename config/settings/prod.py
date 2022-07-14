from .base import *

import environ


DEBUG = False
ALLOWED_HOSTS = ['*']


env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env.prod')


SECRET_KEY = env('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DATABASES_NAME'),
        'USER': env('DATABASES_USER'),
        'PASSWORD': env('DATABASES_PASSWORD'),
        'HOST': 'host.docker.internal',
        'PORT': 3306,
    }
}
