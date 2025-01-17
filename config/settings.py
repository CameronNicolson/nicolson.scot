"""
Django settings for mysite project.

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os
import dj_database_url
from pathlib import Path

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent
# blog/
APPS_DIR = ROOT_DIR

print(ROOT_DIR)
# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
# SECURITY WARNING: don't run with debug turned on in production
DEBUG = os.getenv('DJANGO_DEBUG') != 'FALSE'

# Local time zone. Choices are
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# though not all of them may be available with every OS.
# In Windows, this must be set to your system time zone.
TIME_ZONE = "UTC"
# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = "en-us"
# https://docs.djangoproject.com/en/dev/ref/contrib/sites/
# SITE_ID is Site database table Id, which stores your default details
# such as domain name and brand name
SITE_ID = 1
# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
# https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
LOCALE_PATHS = [str(ROOT_DIR / "locale")]

# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# SECURITY WARNING: keep the secret key used in production a secret!
if DEBUG:
    SECRET_KEY = "testinghello" # <place your secret key here> "testinghello"
    print("DEBUG activated")
else:
    SECRET_KEY = os.getenv("DJANGO_SECRET")

# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts

hosts_str = os.getenv("DJANGO_ALLOWED_HOSTS", "")
host_list = hosts_str.split(",") 
print(host_list)
ALLOWED_HOSTS = [] + host_list

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

POSTGRES_DB = os.getenv("DATABASE_NAME", "django_blog")
POSTGRES_HOST = os.getenv("DATABASE_HOST", "localhost")
POSTGRES_PASSWORD = os.getenv("DATABASE_PASSWORD", "")
POSTGRES_PORT = os.getenv("DATABASE_PORT", "5432")
POSTGRES_USER = os.getenv("DATABASE_USER", "postgres")

DATABASES = {}
DATABASES["default"] = dj_database_url.config(
    default=f"postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

# https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-DEFAULT_AUTO_FIELD
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR / "staticfiles")
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [str(APPS_DIR / "static")]
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = "config.urls"

# APPS
# ------------------------------------------------------------------------------

# apps that require to be top of stack
CRUCIAL_APPS = [
    "daphne",
]

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
]

THIRD_PARTY_APPS = [
    "crispy_forms",
    "crispy_forms_gds",
    "phonenumber_field",
    "taggit",
    "blog_improved",
]

LOCAL_APPS = []

INSTALLED_APPS = CRUCIAL_APPS + DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(APPS_DIR / "media")
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "/media/"

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # https://docs.djangoproject.com/en/dev/ref/settings/#dirs
        "DIRS": [
                ROOT_DIR / "templates",
                APPS_DIR / "templates",
            ],
        # https://docs.djangoproject.com/en/dev/ref/settings/#app-dirs
        "APP_DIRS": True,
        "OPTIONS": {
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "blog_improved.context_processors.navigation",
                "blog_improved.context_processors.site",
            ],
        },
    },
]

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR / "staticfiles")
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [str(APPS_DIR / "static"), str(ROOT_DIR / "public")]
STATICFILES_IGNORE_PATTERNS = [str(ROOT_DIR / "app" / "static")]
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-browser-xss-filter
SECURE_BROWSER_XSS_FILTER = True
# https://docs.djangoproject.com/en/dev/ref/settings/#x-frame-options
X_FRAME_OPTIONS = "SAMEORIGIN"

# CRISPY
# ------------------------------------------------------------------------------
CRISPY_ALLOWED_TEMPLATE_PACKS = ["gds"]
CRISPY_TEMPLATE_PACK = "gds"

# BLOG SETTINGS
# ------------------------------------------------------------------------------
# Main Navigaton
# This handles the navigation bar displayed at the top of your site.
# 
# TITLE is the label shown onscreen 
# URL points to the location
#
# The order displayed is ascending order
# ------------------------------------------------------------------------------
MAIN_NAVIGATION_PAGES = [
    {"TITLE": "Contact", "URL": "contact"},
    {"TITLE": "Services", "URL": "services"},
    {"TITLE": "Projects", "URL": "projects"},
    {"TITLE": "About", "URL": "about"},
    {"TITLE": "External", "URL": "https://fsf.org"},
]

# Contact Me
# ------------------------------------------------------------------------------
# Contact details, one setting changes all contact links.
# every reference called on a page ponits back these settings.
# 
# Useful when I switch email providers, for example.
# All the subsequent mentions of my email are corrected throughout the site. 
# 
# Add as many items as you wish. Format goes "<label>": "<address>"
# ------------------------------------------------------------------------------
CONTACT = {
    "example.com": {
    "DEFAULT_EMAIL": "me@youremail.local", 
    "MATRIX_ID": "@me:matrix.local"
    }
}

ASGI_APPLICATION = os.getenv("ASGI_APP_OBJECT", "")

ADMIN_LOGIN_URL = os.getenv("DJANGO_ADMIN_LOGIN_URL", "admin")
