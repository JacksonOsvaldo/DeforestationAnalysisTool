"""
settings.py

Configuration for Flask app

Important: Place your keys in the secret_keys.py module, 
           which should be kept out of version control.

"""

from google.appengine.api import app_identity
import os

from secret_keys import *
from ee import ServiceAccountCredentials, OAUTH2_SCOPE as EE_OAUTH2_SCOPE
from oauth2client import appengine


DEBUG_MODE = False

# Auto-set debug mode based on App Engine dev environ
if 'SERVER_SOFTWARE' in os.environ and os.environ['SERVER_SOFTWARE'].startswith('Dev'):
    DEBUG_MODE = True

DEBUG = DEBUG_MODE

if DEBUG:
    FT_TABLE = 'imazon_testing.csv'
    FT_TABLE_ID = '2676501'
    EE_API = 'https://earthengine.googleapis.com'
    #EE_API = 'https://earthengine.sandbox.google.com'
    EE_TILE_SERVER = EE_API + '/map/'
    #EE_CREDENTIALS = ServiceAccountCredentials(EE_ACCOUNT, EE_PRIVATE_KEY_FILE)
    EE_CREDENTIALS = None
else:
    EE_API = 'https://earthengine.googleapis.com'
    EE_TILE_SERVER = EE_API + '/map/'
    app_id  = app_identity.get_application_id()
    if app_id == 'imazon-sad-tool':
        FT_TABLE = 'areas'
        FT_TABLE_ID = '1089491'
    elif app_id == 'imazon-prototype':
        FT_TABLE = 'imazon_testing.csv'
        FT_TABLE_ID = '2676501'
    elif app_id == 'sad-training':
        FT_TABLE = 'areas_training'
        FT_TABLE_ID = '1898803'
    elif app_id == 'sad-ee':
        FT_TABLE = 'SAD EE Polygons'
        FT_TABLE_ID = '2949980'
    EE_CREDENTIALS = appengine.AppAssertionCredentials(EE_OAUTH2_SCOPE)


# Set secret keys for CSRF protection
SECRET_KEY = CSRF_SECRET_KEY
CSRF_SESSION_KEY = SESSION_KEY

CSRF_ENABLED = True

