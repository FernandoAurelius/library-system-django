from .base import *

DEBUG = False

ALLOWED_HOSTS = ["bibliotech.floresdev.com.br", "*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": str(os.getenv("DB_NAME")),
        "USER": str(os.getenv("DB_USER")),
        "PASSWORD": str(os.getenv("DB_PASSWORD")),
        "HOST": str(os.getenv("DB_HOST")),
        "PORT": str(os.getenv("DB_PORT")),
    }
}

# Segurança
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
