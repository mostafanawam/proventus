"""
Django settings for proventus project.

Generated by 'django-admin startproject' using Django 3.2.23.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
import os

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4))e3350*f1-047zi3%q_(y56@preh=*3=2j2kz(=sc^(73v2r'

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
]
INSTALLED_APPS += [
    'main'
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

ROOT_URLCONF = 'proventus.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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


WSGI_APPLICATION = 'proventus.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


DATABASE_NAME=os.getenv('DATABASE_NAME','sqlite')
POSTGRES_HOST=os.getenv("POSTGRES_HOST", "127.0.0.1")
POSTGRES_PASSWORD=os.getenv("POSTGRES_PASSWORD", "postgres")
POSTGRES_USER=os.getenv("POSTGRES_USER", "postgres")
POSTGRES_NAME=os.getenv("POSTGRES_NAME", "postgres")
POSTGRES_PORT=os.getenv("POSTGRES_PORT", "5432")
POSTGRES_ENGINE=os.getenv("POSTGRES_ENGINE", 'django.db.backends.postgresql')

if(DATABASE_NAME=="postgres"):
    DATABASES = {
        'default': {
        'ENGINE': POSTGRES_ENGINE,
            'NAME': POSTGRES_NAME,
            'USER': POSTGRES_USER,
            'PASSWORD': POSTGRES_PASSWORD,
            'HOST': POSTGRES_HOST,
            'PORT': POSTGRES_PORT,
            'CONN_MAX_AGE': 20,
        }
    }
    MIGRATION_MODULES={
        'main': f'main.migrations.postgres-dev',
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


MEDIA_ROOT = os.path.join(BASE_DIR, 'assets')

# Define the base URL to serve media files from
MEDIA_URL = '/assets/'

CELERY_BROKER_URL=os.getenv("CELERY_BROKER_URL", 'amqp://guest:guest@localhost:5672/')
RESULT_BACKEND_URL=os.getenv("RESULT_BACKEND_URL", 'amqp://guest:guest@localhost:5672/')

accept_content = ['json']  # Specify accepted content types (e.g., JSON)
task_serializer = 'json'  # Task serialization format
result_serializer = 'json'  # Result serialization format

# Concurrency settings (adjust as needed)
CELERY_BROKER_CONNECTION_RETRY = True  # Deprecated, use the new setting below
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True  # Retains existing behavior on startup
 # Maximum tasks a worker can execute before it's replaced
task_time_limit = 1200  # Maximum time a task can run (in seconds)

CELERY_broker_connection_retry_ON_STARTUP = True