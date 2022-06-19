import os
from pathlib import Path
# import django_heroku
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ.get('SECRET_KEY')

SECRET_KEY = 'django-insecure-!4@is-xp5+mfc^ign&hgit0z2_r7o$n7manz=_o3e7o*76)9=@'

# SECURITY WARNING: don't run with debug turned on in production!

# DEBUG = bool(int(os.environ.get('DEBUG', default=1)))

DEBUG = True

if DEBUG:
    MEDIA_HOST = "http://18.195.66.145"
else:
    MEDIA_HOST = "http://18.195.66.145"

# ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS').split('')
ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = ['127.0.0.1', '18.156.129.57', '18.195.66.145', 'stepbook.co']
# Application definition

INSTALLED_APPS = [
    'admin_interface',
    'colorfield',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'djoser',

    'taggit',
    'adminsortable2',
    'Test',

    'Countries',
    'Cities',
    'Foods',
    'CostOfLiving',
    'Transport',
    'Language',
    'Apps',
    'Score',
    'Visit',
    'Rent',
    'IMAGES',
    'Search',
    'EatPlace',
    'Z_Meta',

]

X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]


CORS_ALLOWED_ORIGINS = [
    "http://stepbook.co",
    "https://stepbook.co",
    "http://localhost:8080",
    "http://127.0.0.1:8000",
    "http://18.156.129.57",
    "http://localhost",
    "http://35.158.203.11",
    "http://localhost:1337",
    "http://localhost:80",
]

CSRF_TRUSTED_ORIGINS = [
    "http://stepbook.co",
    "https://stepbook.co",
    "http://localhost:1337",
    "http://localhost:80",
    "http://127.0.0.1:8000",
    "http://18.156.129.57",
    "http://localhost:8080",
    "http://localhost",
    "http://35.158.203.11",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# django_heroku.settings(locals())


