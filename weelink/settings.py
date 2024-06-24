
from pathlib import Path
import os

import environ
import dj_database_url
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2apmb@wxdeh_qj@3x9p=aav^tl1eh2bc2qz(r-%4lrb-j7k$qg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG')
# DEBUG = False

ALLOWED_HOSTS = ['*', '.onrender.com', '127.0.0.1']
CSRF_TRUSTED_ORIGINS = ["https://weelink.onrender.com","http://localhost:8000"]



# Application definition

INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions', 
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
    'core',
    'nested_admin',
    'accounts',
    'channels',
    'chat',
    'channels_redis',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'weelink.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                 'weelink.context_processors.base_template_data',
            ],
        },
    },
]

WSGI_APPLICATION = 'weelink.wsgi.application'



# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


# Development database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Deployment database


database_url = os.environ.get('DATABASE_URL')
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'railway',
#         'USER': 'postgres',
#         'PASSWORD': 'OAyuPMgOPOEtUtqsgXKjFNbRQFdVZMTz',
#         'HOST': 'roundhouse.proxy.rlwy.net',
#         'PORT': '56979',
#     }
# }




# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATICFILES_STORAGE="whitenoise.storage.CompressedManifestStaticFilesStorage"


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'



ASGI_APPLICATION = 'weelink.asgi.application'



# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/' 


# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels.layers.InMemoryChannelLayer',
#         # 'CONFIG': {
#         #     'hosts': [('127.0.0.1', 6379)],
#         # }
#     }
# }

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [('redis://default:kIxFUNukMANrLZtmJowPQDkHYZpNTvep@monorail.proxy.rlwy.net:21756')],
        },
    },
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://default:kIxFUNukMANrLZtmJowPQDkHYZpNTvep@monorail.proxy.rlwy.net:21756',  # Adjust the location if Redis is running elsewhere
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

CACHE_TTL = 60 * 15