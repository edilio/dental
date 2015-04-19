
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

try:
    import pymysql

    pymysql.install_as_MySQLdb()
except ImportError:
    pass

import dotenv

env_file = os.path.join(BASE_DIR, '.env')
#
dotenv.read_dotenv(env_file)

DEBUG = bool(int(os.environ.get('DEBUG', '0')))
TEMPLATE_DEBUG = DEBUG
IN_DEV = bool(int(os.environ.get('IN_DEV', '0')))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^n%f8rti)9fz_68r)xs13n4($r$6&)q@-74xcj5*th$c6c(pnp'

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fern',
    'marketing',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'dental.urls'

WSGI_APPLICATION = 'dental.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    },
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DBASE_NAME'),
        'USER': os.environ.get('DBASE_USER'),
        'PASSWORD': os.environ.get('DBASE_PASSWORD'),
        'HOST': os.environ.get('DBASE_HOST') or ''
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = '/var/www/html/wmedia/dental/static/'


TEMPLATE_DIRS = (
    (os.path.join(BASE_DIR, 'fern/templates')),
    (os.path.join(BASE_DIR, 'marketing/templates')),
)
