from .base import *

import environ


DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'host.docker.internal']


env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env.local')


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
