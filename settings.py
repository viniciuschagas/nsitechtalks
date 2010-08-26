# -*- coding: utf-8 -*-
# Django settings for nsitechtalks project.
import os
PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Vinícius Chagas', 'vinimaster@gmail.com'),
    ('Rodrigo Manhães', 'rmanhaes@gmail.com'),
    ('Gustavo Rezende', 'nsigustavo@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT_PATH,'nsitechtalks.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'America/Sao_Paulo'

LANGUAGE_CODE = 'pt-br'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = os.path.join(PROJECT_ROOT_PATH,'site_media')

MEDIA_URL = '/site_media'

ADMIN_MEDIA_PREFIX = '/admin_media/'

SECRET_KEY = '*l*mzug)p_cgt*aze#j-07qbp1e*xpw^5gm+hg*zw_y9oyap4!'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
)

ROOT_URLCONF = 'nsitechtalks.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT_PATH,'templates'),
    os.path.join(PROJECT_ROOT_PATH,'techtalks/templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'pagination',
    'nsitechtalks.techtalks',
)


EMAIL_HOST="server.com"#Configurar servidor de e-mail
EMAIL_PORT="25"
EMAIL_HOST_USER=""
EMAIL_HOST_PASSWORD=""
EMAIL_USE_TLS=False