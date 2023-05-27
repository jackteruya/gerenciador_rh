from .settings import *  # noqa

CACHES = {'default': {'BACKEND': 'django.core.cache.backends.dummy.DummyCache'}}
DEFAULT_FILE_STORAGE = 'inmemorystorage.InMemoryStorage'
