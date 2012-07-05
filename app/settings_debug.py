from settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES['default'].update({
    'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
    'NAME': 'database.sqlite',                      # Or path to database file if using sqlite3.
    'USER': '',                      # Not used with sqlite3.
    'PASSWORD': '',                  # Not used with sqlite3.
    'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
    'PORT': '',  
    })



MEDIA_URL = ''
MEDIA_ROOT = '../'
STATIC_ROOT = ''
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS =(
      os.path.join(SITE_ROOT, 'static'),
      os.path.join(SITE_ROOT, '..', 'less'),
  )
