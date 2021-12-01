from academiaAdmin.settings.settings import *

DEBUG = True

SECRET_KEY = 'n#8(pi2zl9d44k!lo2z46%zm-5%uagyo+=r-fy9muyw13+)ow@'

# Alterar para o IP do ambiente de produção quando houver.
ALLOWED_HOSTS = ['pilatesapp.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
