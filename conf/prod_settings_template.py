_user = '{{webuser}}'
_host = '{{host}}'

ALLOWED_HOSTS = [_host]
SECURE_PROXY_SSL_HEADER = ('HTTP_X_SCHEME', 'https')
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True

FROM_EMAIL = "noreply@%s" % _host
DEFAULT_FROM_EMAIL = FROM_EMAIL
EMAIL_SUBJECT_PREFIX = '[%s] ' % _user.upper()

ADMINS = (
    ('{{user}}', '{{user}}@localhost'),
)

MANAGERS = ADMINS

SECRET_KEY = '{{secret_key}}'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': _user,
        'USER': _user,
        'PASSWORD': _user,
        'HOST': 'localhost',
        'PORT': '',
    },
}
