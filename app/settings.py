# Django settings for gapbird project.

import os

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))


DEBUG = False 
TEMPLATE_DEBUG = DEBUG

INTERNAL_IPS = ('127.0.0.1' ,)
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

USER_I18N = True


MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
    }
}



# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Berlin'

_ = lambda s: s 

LANGUAGES = (
    ('en', _(u'English')),
#    ('de', _(u'German')),
#    ('es', _(u'Spanish'))
#    ('fr', _(u'French')),
#    ('ru', _(u'Russian')),
)

# If you want to use localurl

#PREFIX_DEFAULT_LOCALE = True
#LOCALEURL_USE_ACCEPT_LANGUAGE = True

#LOCALE_INDEPENDENT_PATHS = (
#    r'^/admin/',
#    r'^/rosetta/',
#    r'^/markitup/',
#)

# in cas you feel like making rosetta reload your content
# ROSETTA_RELOAD = True

# use the hostname given by nginx
USE_X_FORWARDED_HOST = True

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = 'media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = 'https://s3.amazonaws.com/__EXAMPLE__/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = 'https://s3.amazonaws.com/__EXAMPLE__/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = 'http://s3.amazonaws.com/__EXAMPLE__/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, 'static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'gdks$=f$vq=a959p6=sd!a7ds3le%)_!)$okeg)03y(vpih8-c'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'gapbird.base.utils.process_template',
    'gapbird.cms.context_processors.menu',
    'django.core.context_processors.csrf',
    'django.contrib.auth.context_processors.auth',
)

MIDDLEWARE_CLASSES = (
    'localeurl.middleware.LocaleURLMiddleware', # gotta be *before* CommonMiddleware and there shall not be any builtin LocaleMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(SITE_ROOT, 'templates')
)

#guardian
ANONYMOUS_USER_ID = -1

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# SETUP to go through amazon AWS/SES, specify login data here
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
EMAIL_PORT = 25
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = "no-reply@example.com"

#userena setup
AUTH_PROFILE_MODULE = "base.UserProfile"

LOGIN_REDIRECT_URL = USERENA_SIGNIN_REDIRECT_URL = '/'
USERENA_ACTIVATION_REQUIRED = True
USERENA_DISABLE_PROFILE_LIST = True
USERENA_HIDE_EMAIL = True
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'

USERENA_MUGSHOT_DEFAULT = "wavatar"
USERENA_WITHOUT_USERNAMES = True
USERENA_DISABLE_PROFILE_LIST = False
USERENA_DEFAULT_PRIVACY = 'open'

#markup
MARKITUP_SET = 'markitup/sets/textile'
MARKITUP_SKIN = 'markitup/skins/simple'
MARKITUP_FILTER = ('django.contrib.markup.templatetags.markup.textile', {})


AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_STORAGE_BUCKET_NAME = ''



INSTALLED_APPS = (
#    'localeurl', # GOTTA BE FIRST!!!!
#    'mothertongue',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.markup',
    'markitup',
    'gunicorn',
    'storages',
    'bootstrap',
    'guardian',
    'userena',
    'south',
    # project
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
	'file':{
	    'level': 'DEBUG',
	    'class': 'logging.FileHandler',
            'filename': 'debug.log',
	},
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
#            'formatter': 'simple'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'gapbird': {
            'handlers': ['console'],
            'level': 'INFO',
        },
 
    }
}


#### APP_SPECIFIC:

