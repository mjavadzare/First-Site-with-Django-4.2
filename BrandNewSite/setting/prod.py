from BrandNewSite.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
from decouple import config

SECRET_KEY = config("SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []
#INSTALLED_APPS = []

# sites framework
SITE_ID = 2

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        }
    }
}

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True


STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media' 

STATICFILES_DIRS = [
    BASE_DIR / "statics"
]

MAINTENANCE_MODE = True

import django.conf
#compressor settings
django.conf.settings.COMPRESS_ENABLED = False
django.conf.settings.COMPRESS_URL = STATIC_URL
django.conf.settings.COMPRESS_ROOT = STATIC_ROOT
django.conf.settings.COMPRESS_OUTPUT_DIR = 'CACHE'
django.conf.settings.COMPRESS_FILTERS = {'css': ['compressor.filters.css_default.CssAbsoluteFilter',
                                                  'compressor.filters.cssmin.rCSSMinFilter'],
                                                    'js': ['compressor.filters.jsmin.rJSMinFilter']}
django.conf.settings.COMPRESS_YUGLIFY_CSS_ARGUMENTS = {'css':['compressor.filters.cssmin.CSSCompressorFilter',]}
django.conf.settings.COMPRESS_TEMPLATE_FILTER_CONTEXT = {'js':['compressor.filters.jsmin.rJSMinFilter']}
django.conf.settings.COMPRESS_PRECOMPILERS = ()
django.conf.settings.COMPRESS_STORAGE = 'compressor.storage.CompressorFileStorage'
# django.conf.settings.COMPRESS_PARSER = 'compressor.parser.AutoSelectParser'
django.conf.settings.COMPRESS_CACHE_BACKEND = "default"
django.conf.settings.COMPRESS_REBUILD_TIMEOUT = 2592000
django.conf.settings.COMPRESS_MINT_DELAY = 30
django.conf.settings.COMPRESS_MTIME_DELAY = 10
django.conf.settings.COMPRESS_CACHEABLE_PRECOMPILERS = ()
django.conf.settings.COMPRESS_CACHE_KEY_FUNCTION = 	'compressor.cache.simple_cachekey'
django.conf.settings.COMPRESS_OFFLINE = False
django.conf.settings.COMPRESS_OFFLINE_TIMEOUT = 31536000

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)
