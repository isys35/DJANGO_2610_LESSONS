from classroom.settings._base import *

DEBUG = False

ALLOWED_HOSTS = [
    get_secret("HOST_IP_ADDRESS")
]

STATIC_ROOT = BASE_DIR / "static_root"