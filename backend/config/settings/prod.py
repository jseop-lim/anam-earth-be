from .base import *

import environ


DEBUG = False
ALLOWED_HOSTS = [
    'anam-earth.jseoplim.com',
    'www.anam-earth.jseoplim.com',
    '43.200.76.8',
    'ec2-43-200-76-8.ap-northeast-2.compute.amazonaws.com',
    '127.0.0.1'
]

# USE_X_FORWARDED_HOST = True
# FORCE_SCRIPT_NAME = '/api'
#
# STATIC_URL = 'api/static/'


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


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',  # change debug level as appropiate
            'propagate': False,
        },
    },
}
