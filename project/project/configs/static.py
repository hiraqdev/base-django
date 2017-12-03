import os 

STATIC_URL = os.environ.get('STATIC_URL')
STATIC_ROOT = os.environ.get('STATIC_ROOT')

MEDIA_URL = os.environ.get('MEDIA_URL')
MEDIA_ROOT = os.environ.get('MEDIA_ROOT')