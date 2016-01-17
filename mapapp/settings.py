import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = [
    'map.10x.org.il',
]

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'django_extensions',
    'django.contrib.sites',
    'authtools',
    'bootstrap3',
    'floppyforms',
    # for floppy forms widgets, mmake sure to run manage.py collectstatic once you deploy your project.
    'leaflet',
    'django_social_share',
    'users',
    'librarian',
    'clientapp',
    'home',
    'django.contrib.admin',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'mapapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mapapp.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'mapapp',
        'USER': 'mapapp',
        'HOST': 'localhost',
        'PASSWORD': 'mapapp',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'he'

TIME_ZONE = 'Asia/Jerusalem'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = "users.User"

LOGIN_REDIRECT_URL = "/lib/"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'collected-static')
STATIC_URL = '/static/'

LEAFLET_CONFIG = {
    'SPATIAL_EXTENT': (32, 29, 36, 33.5),
    'DEFAULT_CENTER': (35.093303, 31.976406),
    'DEFAULT_ZOOM': 8,

    'TILES': [

        ('OVI Satellite',
         'http://maptile.maps.svc.ovi.com/maptiler/maptile/newest/satellite.day/{z}/{x}/{y}/256/png8',
         'OVI maps'),

        ('OpenStreet map',
         'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
         'OpenStreet Map'),

        ('MapQuest Open Aerial',
         'http://otile1.mqcdn.com/tiles/1.0.0/sat/{z}/{x}/{y}.jpg',
         'MapQuest Open Aerial'),

        ('Israel Hiking Trails',
         'http://osm.org.il/IsraelHiking/Tiles/{z}/{x}/{y}.png',
         'Israel Hiking Trails'),
    ],

    'ATTRIBUTION_PREFIX': 'סיפורי דרכים',
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },

    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },

    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'null': {
            'class': 'logging.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },

    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'django': {
            'handlers': ['console'],
        },
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['mail_admins', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
        'urllib3': {
            'level': 'WARN',
        },
        'py.warnings': {
            'handlers': ['console'],
            'level': 'ERROR',
        },
    }
}

if os.name == 'nt':
    OSGEO4W = r"C:\OSGeo4W"
    os.environ['OSGEO4W_ROOT'] = OSGEO4W
    os.environ['GDAL_DATA'] = OSGEO4W + r"\share\gdal"
    os.environ['PROJ_LIB'] = OSGEO4W + r"\share\proj"
    os.environ['PATH'] = OSGEO4W + r"\bin;" + os.environ['PATH']

try:
    from .local_settings import *
except ImportError:
    pass
