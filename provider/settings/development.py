"""
Django development settings for provider project.
"""

from .base import *
from django.utils.translation import ugettext_lazy as _

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "-a*3%io#m$ys=8=$^tnhr9wl#s_!$m$e$g=0kv-i_jquk^8pk="

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1"]

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# Static files
STATIC_ROOT = os.path.join(BASE_DIR, "site_media", "static")
MEDIA_ROOT = os.path.join(BASE_DIR, "site_media", "media")

# i18n
LANGUAGES = (
    ("en", _("English")),
    ("fr", _("French")),
    ("es", _("Spanish")),
    ("de", _("German")),
    ("pt", _("Portuguese")),
)

# Email
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Django OAuth Toolkit
# SECURITY WARNING: don't run with CORS_ORIGIN_ALLOW_ALL turned on in production!
CORS_ORIGIN_ALLOW_ALL = True
# Important to avoid conflicts with the client app
# also setting its own `sessionid` cookie.
SESSION_COOKIE_NAME = "oauth2server_sessionid"
