# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/
import os 
from django.core.management.utils import get_random_secret_key

def _parse_debug_env():
    debug = os.environ.get('DEBUG')
    return debug == 'On'

def _parse_allowed_hosts_env():
    hosts = os.environ.get('ALLOWED_HOSTS')
    return hosts.split(',')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_random_secret_key()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = _parse_debug_env() 

ALLOWED_HOSTS = _parse_allowed_hosts_env() 