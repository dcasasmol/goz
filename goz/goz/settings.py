"""
Django settings for goz project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import os
import datetime


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yxz!---3eq&^azfgc5&-$87&$405xd#m8_%mr9^gkh9*o@*uq3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

ADMINS = (
    # ('David Casas Molina', 'david.casasmolina@gmail.com'),
)

MANAGERS = ADMINS

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'south',
    'dbapi',
    'foursquareapi',
    'utils',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'goz.urls'

WSGI_APPLICATION = 'goz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # Or path to database file if using sqlite3.
        'NAME': 'goz_database',
        # The following settings are not used with sqlite3:
        'USER': 'django_goz',
        'PASSWORD': 'U6NTQ3md',
        # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'HOST': 'localhost',
        # Set to empty string for default.
        'PORT': '',
    }
}

# Django superuser info:
# user: admin
# email: admin@gameofzones.es
# password: 6VKPYq3z

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
  ('es', 'Spanish'),
  ('en', 'English'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

LOCALE_PATHS = (
  os.path.join(BASE_DIR, 'locale'),
)

LOGGER_NAME = 'goz'
LOG_MAXBYTES = 1024*1024*10 #10 MB
LOG_BACKUPCOUNT = 5
LOG_PATH = os.path.join(BASE_DIR, 'logs')
LOG_FILENAME = '%s-%s' % (datetime.date.today().strftime("%Y%m%d"),
                              __package__)

LOGGING = {
  'version': 1,
  'disable_existing_loggers': False,
  'formatters': {
    'verbose': {
      'format' : "[%(asctime)s] %(pathname)s:%(lineno)d [%(levelname)s] %(message)s",
      'datefmt' : "%d-%b-%Y %H:%M:%S"
    },
    'simple': {
      'format': '%(levelname)s %(message)s'
    },
  },
  'handlers': {
    'general': {
      'level': 'INFO',
      'formatter': 'verbose',
      'class' : 'logging.handlers.RotatingFileHandler',
      'filename' : '%s/%s.log' % (LOG_PATH, LOG_FILENAME),
      'encoding': 'utf8',
      'maxBytes': LOG_MAXBYTES,
      'backupCount': LOG_BACKUPCOUNT,
    },
    'errors': {
      'level': 'ERROR',
      'formatter': 'verbose',
      'class' : 'logging.handlers.RotatingFileHandler',
      'filename' : '%s/%s-errors.log' % (LOG_PATH, LOG_FILENAME),
      'encoding': 'utf8',
      'maxBytes': LOG_MAXBYTES,
      'backupCount': LOG_BACKUPCOUNT,
    },
  },
  'loggers': {
    LOGGER_NAME: {
      'handlers': ['general', 'errors'],
      'level': 'DEBUG',
    },
  }
}
