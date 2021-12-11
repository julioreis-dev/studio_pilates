from academiaAdmin.settings.settings import *
import dj_database_url


DEBUG = True

SECRET_KEY = 'n#8(pi2zl9d44k!lo2z46%zm-5%uagyo+=r-fy9muyw13+)ow@'

# Alterar para o IP do ambiente de produção quando houver.
ALLOWED_HOSTS = ['pilatesapp.herokuapp.com']

DATABASES = {
    'default': dj_database_url.config()
}
