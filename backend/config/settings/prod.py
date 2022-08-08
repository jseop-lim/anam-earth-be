from .base import *

import environ


DEBUG = False
ALLOWED_HOSTS = [
    'anam-earth.jseoplim.com',
    'www.anam-earth.jseoplim.com',
    '43.200.76.8',
    '127.0.0.1'
]

USE_X_FORWARDED_HOST = True
FORCE_SCRIPT_NAME = '/api'

STATIC_URL = FORCE_SCRIPT_NAME + STATIC_URL


env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env.prod')

SECRET_KEY = env('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('MYSQL_DATABASE'),
        'USER': env('MYSQL_USER'),
        'PASSWORD': env('MYSQL_PASSWORD'),
        'HOST': '43.200.76.8',
        'PORT': 3306,
    }
}
