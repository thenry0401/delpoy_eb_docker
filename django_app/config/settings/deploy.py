from .base import *


config_secret_debug = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

# WSGI application
WSGI_APPLICATION = 'config.wsgi.deploy.application'

# Static URLs
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

DEBUG = False
ALLOWED_HOSTS = config_secret_debug['django']['allowed_hosts']
