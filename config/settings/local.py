from .base import *


DATABASES = {
    'default': env.db(),
}
DEBUG = env.bool("DEBUG", default=True)
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
INTERNAL_IPS = [
    "127.0.0.1",
]