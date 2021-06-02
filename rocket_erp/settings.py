import datetime
import os

from .env import env
from .env import root

BASE_DIR = root()


SECRET_KEY = env("SECRET_KEY")

DEBUG = env("DEBUG")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
AUTH_USER_MODEL = "accounts.Account"

INSTALLED_APPS = [
    # core apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # third party apps
    "rest_framework",
    "rest_framework_jwt",
    "bootstrap4",
    # apps
    "rocket_erp.apps.accounts",
    "rocket_erp.apps.api",
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

ROOT_URLCONF = "rocket_erp.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            "rocket_erp/templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "rocket_erp.wsgi.app"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth."
                "password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth."
                "password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth."
                "password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth."
                "password_validation.NumericPasswordValidator",
    },
]

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework."
                                "pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_AUTHENTICATION_CLASSES": (
        #     'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        #     'rest_framework.permissions.IsAuthenticated',
        "rest_framework.permissions.AllowAny",
    ),
}

JWT_AUTH = {
    "JWT_VERIFY": True,
    "JWT_VERIFY_EXPIRATION": True,
    "JWT_EXPIRATION_DELTA": datetime.timedelta(seconds=3000),
    "JWT_AUTH_HEADER_PREFIX": "Bearer",
}

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "ru"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "rocket_erp", "static"),)
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

ADMIN_MEDIA_PREFIX = "/static/admin/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

DISABLE_USERNAME = True
LOGIN_VIA_EMAIL = True
LOGIN_URL = "accounts:login"
USE_REMEMBER_ME = True
SIGN_UP_FIELDS = ["email", "password1", "password2"]
