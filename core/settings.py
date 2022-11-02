"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from telnetlib import AUTHENTICATION

# #cloudinary imports 
# import cloudinary 
# import cloudinary.uploader
# import cloudinary.api

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

  # SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ei)nzvhn((#p-^_0k+kz8p+07l$*&0n&_uexnd*hh$34&wr-xs'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = ["bookly.com",'localhost','127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'accounts',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # local
    "books",
    "actions",
    # 3d parites
    "crispy_forms",
    "crispy_bulma",
    "django_browser_reload",
    # auth

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    ##tailwind 
    # 'tailwind',
    # 'theme',

    ##services
    'cloudinary_storage',
    'cloudinary',
    ##https
    'django_extensions',
    'compressor'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # added middlewares
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/"templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# crispy forms settings

CRISPY_ALLOWED_TEMPLATE_PACKS = ("bulma", )

CRISPY_TEMPLATE_PACK = "bulma"


# REDIRECT
LOGIN_REDIRECT_URL = "accounts:profile"
LOGIN_URL = "accounts:login"
LOGOUT_URL = "accounts:logout"
# Authentication backends
AUTHENTICATION_BACKENDS = ["django.contrib.auth.backends.ModelBackend",
                           "accounts.authentication.EmailAuthBackend",
                           "allauth.account.auth_backends.AuthenticationBackend"
                           ]
# mail jet
# MAIL_API_KEY = os.getenv("MAIL_API_KEY")
# MAIL_SECRET_KEY = os.getenv("MAIL_SECRET_KEY")
# email settings

# EMAIL_HOST="smtp.gmail.com"
# EMAIL_HOST_PASSWORD=os.getenv("EMAIL_PASSWORD")
# EMAIL_HOST_USER=os.getenv("EMAIL_USER")
# EMAIL_USE_TLS=True
# EMAIL_POST=587
EMAIL_BACKEND = "anymail.backends.mailjet.EmailBackend"
ANYMAIL = {
    "MAILJET_API_KEY": os.getenv('MAIL_API_KEY'),
    "MAILJET_SECRET_KEY": os.getenv('MAIL_SECRET_KEY'),
}

DEFAULT_FROM_EMAIL = 'jobly@email.com'


# media files
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / "media/"


SITE_ID = 2

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile', 'user_friends'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'link',
            'gender',
        ],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': 'path.to.callable',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.12',
    },
}
##cloudinary config 

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv("CLOUDINARY_NAME"),
    'API_KEY': os.getenv("CLOUDINARY_KEY") ,
    'API_SECRET': os.getenv("CLOUDINARY_SECRET") 
}

#tailwind css 

# TAILWIND_APP_NAME = 'theme'
# INTERNAL_IPS = [
#     "127.0.0.1",
# ]

#composer settings 

COMPRESS_ROOT = BASE_DIR / 'static'
COMPRESS_ENABLED = True
STATICFILES_FINDERS = ('compressor.finders.CompressorFinder',)
#redis settings 
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB=0

if os.getenv("DEVELOPMENT_MODE")=='false':
    from .production_settings import *
