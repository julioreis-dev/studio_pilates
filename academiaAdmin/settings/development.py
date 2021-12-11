import dj_database_url

from academiaAdmin.settings.settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n#8(pi2zl9d44k!lo2z46%zm-5%uagyo+=r-fy9muyw13+)ow@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': dj_database_url.config()
}
