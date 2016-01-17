DEBUG = True
TEMPLATE_DEBUG = True

SECRET_KEY = '{{secret_key}}'
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.contrib.gis.db.backends.postgis',
#         'NAME': 'mapapp',
#         'HOST': 'localhost',
#     }
# }
