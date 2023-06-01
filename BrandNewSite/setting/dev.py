from BrandNewSite.settings import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
from decouple import config

#SECRET_KEY = config("SECRET_KEY")
SECRET_KEY = 'django-insecure-y@-4ep(=of473n=0f$10p6t1oa3g5fprcbr@keqizqpeky3ag%'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#INSTALLED_APPS = []

# from BrandNewSite.settings import LOGIN_URL , LOGIN_REDIRECT_URL
# #allauth configuration
# ACCOUNT_ADAPTER = "allauth.account.adapter.DefaultAccountAdapter"
# ACCOUNT_AUTHENTICATION_METHOD = "username_email"
# ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True
# ACCOUNT_CONFIRM_EMAIL_ON_GET = False
# ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_URL
# ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = None
# ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
# ACCOUNT_EMAIL_CONFIRMATION_HMAC = True
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_EMAIL_VERIFICATION = "optional" #Determines the e-mail verification method during signup – choose one of "mandatory", "optional", or "none".
# ACCOUNT_EMAIL_SUBJECT_PREFIX = "[Site]"
# ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"
# ACCOUNT_EMAIL_CONFIRMATION_COOLDOWN = 180
# ACCOUNT_EMAIL_MAX_LENGTH = 254
# ACCOUNT_MAX_EMAIL_ADDRESSES = None #Note that if you set the maximum to 1, users will not be able to change their email address as they are unable to add the new address, followed by removing the old address.
# ACCOUNT_FORMS = {'add_email': 'allauth.account.forms.AddEmailForm',
#                     'change_password': 'allauth.account.forms.ChangePasswordForm',
#                     'disconnect': 'allauth.socialaccount.forms.DisconnectForm',
#                     'login': 'allauth.account.forms.LoginForm',
#                     'reset_password': 'allauth.account.forms.ResetPasswordForm',
#                     'reset_password_from_key': 'allauth.account.forms.ResetPasswordKeyForm',
#                     'set_password': 'allauth.account.forms.SetPasswordForm',
#                     'signup': 'allauth.account.forms.SignupForm',
#                     'signup': 'allauth.socialaccount.forms.SignupForm',
#                 }
# ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
# ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 240
# ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = False
# ACCOUNT_LOGOUT_ON_GET = False
# ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
# ACCOUNT_LOGIN_ON_PASSWORD_RESET = False
# ACCOUNT_LOGOUT_REDIRECT_URL = '/'
# ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = False
# ACCOUNT_PRESERVE_USERNAME_CASING = True
# ACCOUNT_PREVENT_ENUMERATION = True
# ACCOUNT_RATE_LIMITS = {
#     # Change password view (for users already logged in)
#     "change_password": "5/m",
#     # Email management (e.g. add, remove, change primary)
#     "manage_email": "10/m",
#     # Request a password reset, global rate limit per IP
#     "reset_password": "20/m",
#     # Rate limit measured per individual email address
#     "reset_password_email": "5/m",
#     # Password reset (the view the password reset email links to).
#     "reset_password_from_key": "20/m",
#     # Signups.
#     "signup": "20/m",
#     # NOTE: Login is already protected via `ACCOUNT_LOGIN_ATTEMPTS_LIMIT`
# }
# ACCOUNT_SESSION_REMEMBER = None
# ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = False
# ACCOUNT_SIGNUP_FORM_CLASS = None
# ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
# ACCOUNT_SIGNUP_REDIRECT_URL = LOGIN_REDIRECT_URL
# ACCOUNT_TEMPLATE_EXTENSION  = "html"
# ACCOUNT_USERNAME_BLACKLIST = ['admin',]
# ACCOUNT_UNIQUE_EMAIL = True
# #ACCOUNT_USER_DISPLAY = 
# ACCOUNT_USER_MODEL_EMAIL_FIELD = 'email'
# ACCOUNT_USER_MODEL_USERNAME_FIELD  = 'username'
# ACCOUNT_USERNAME_MIN_LENGTH = 4
# ACCOUNT_USERNAME_REQUIRED = True
# ACCOUNT_USERNAME_VALIDATORS = None
# SOCIALACCOUNT_ADAPTER = "allauth.socialaccount.adapter.DefaultSocialAccountAdapter"
# SOCIALACCOUNT_AUTO_SIGNUP = True
# SOCIALACCOUNT_EMAIL_VERIFICATION = ACCOUNT_EMAIL_VERIFICATION
# SOCIALACCOUNT_EMAIL_REQUIRED = ACCOUNT_EMAIL_REQUIRED
# SOCIALACCOUNT_FORMS = {}
# SOCIALACCOUNT_LOGIN_ON_GET = False
# # Provider specific settings
# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         # For each OAuth based provider, either add a ``SocialApp``
#         # (``socialaccount`` app) containing the required client
#         # credentials, or list them here:
#         'APP': {
#             'client_id': '123',
#             'secret': '456',
#             'key': ''
#         }
#     }
# }
# SOCIALACCOUNT_QUERY_EMAIL = ACCOUNT_EMAIL_REQUIRED
# #SOCIALACCOUNT_SOCIALACCOUNT_STR = 
# SOCIALACCOUNT_STORE_TOKENS = False


# sites framework
SITE_ID = 2


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media' 

STATICFILES_DIRS = [
    BASE_DIR / "statics"
]

MAINTENANCE_MODE = False

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

# important
COMPRESS_ENABLED = os.environ.get('COMPRESS_ENABLED', False)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)
