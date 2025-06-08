from .base import *

DATABASES = {
    'default': env.db(),
}
DEBUG = False
ALLOWED_HOSTS = []