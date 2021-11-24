
from .base import *

# Database
# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
DEBUG = bool(os.environ.get('DJANGO_DEBUG', True))
SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',  'hy0uto&3_tjiezg=8+ml90#%p0+njk%qf_+^*)lb^1q4a2ugd@')
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
