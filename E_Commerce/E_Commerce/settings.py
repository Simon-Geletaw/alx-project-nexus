"""
Django settings for E_Commerce project.
"""

from pathlib import Path
from environ import Env, environ
<<<<<<< Updated upstream
from datetime import timedelta
import os
import sys

=======
import os
>>>>>>> Stashed changes
env = Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Add the 'apps' directory to sys.path so Django can find the apps without the 'apps.' prefix
sys.path.append(os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

<<<<<<< Updated upstream
# Read environment variables
=======
# SECURITY WARNING: keep the secret key used in production secret!
>>>>>>> Stashed changes
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party apps
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_spectacular',
    'django_filters',

    # Local apps
    'apps.accounts',
    'apps.categories',
<<<<<<< Updated upstream
    'apps.products',
=======
    'rest_framework',
    'rest_framework_simplejwt',
>>>>>>> Stashed changes
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'E_Commerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'E_Commerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': env('DB_ENGINE'),
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
<<<<<<< Updated upstream

# Custom User Model
# The format must be 'app_label.ModelName'. 
# Even though the path is apps.accounts, the app_label is 'accounts'.
AUTH_USER_MODEL = 'accounts.AccountsUser'
=======
AUTH_USER_MODEL = 'apps.accounts.AccountsUser'
INSTALLED_APPS = [
    # Other apps
    'rest_framework_simplejwt',
]
>>>>>>> Stashed changes

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
<<<<<<< Updated upstream
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ),
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'E_Commerce API',
    'DESCRIPTION': 'API documentation for E_Commerce',
    'VERSION': '1.0.0',
}

# Simple JWT Settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=env.int('ACCESS_TOKEN_LIFETIME', default=50000)),
    'REFRESH_TOKEN_LIFETIME': timedelta(minutes=env.int('REFRESH_TOKEN_LIFETIME', default=1440)),
}
=======
}
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': env.int('ACCESS_TOKEN_LIFETIME', default=5),  # in minutes
    'REFRESH_TOKEN_LIFETIME': env.int('REFRESH_TOKEN_LIFETIME', default=1440),  # in minutes (1 day)
}
>>>>>>> Stashed changes
