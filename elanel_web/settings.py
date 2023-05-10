
from pathlib import Path
import os
import environ

env=environ.Env()
environ.Env.read_env()
 
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = os.environ.get("SECRET_KEY")
SECRET_KEY="()ue$zj3&su3$+1a#p0r8=umkc-v^la2=5zu6#91r^pi5&#qil"
# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG =os.environ.get("DEBUG")
DEBUG =True

ALLOWED_HOSTS = ['181.215.135.171','www.elanelsys.com','elanelsys.com','*']

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST= "c1611768.ferozo.com"
EMAIL_USE_SSL = True
EMAIL_PORT = 465
# EMAIL_TIMEOUT = None
EMAIL_HOST_USER="solicitudesclientes@elanelsys.com"
EMAIL_HOST_PASSWORD="klf781CL*"

LOGGING = {
	"version": 1,
	"disable_existing_loggers": False,
	"handlers": {
		"file": {
			"level": "DEBUG",
			"class": "logging.FileHandler",
			"filename": "/home/elanelweb/elanal_web/errors_production/error.log",
		 },
	},
	"loggers": {
		"django": {
			"handlers": ["file"],
			"level": "DEBUG",
			"propagate": True,
		},
	},
}

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'import_export',
    'market',
    'rangefilter',
    'django_quill',
    'django.contrib.humanize',
]

JAZZMIN_SETTINGS ={
    "site_title": "ELANEL",
    "login_logo": "images/fwd/icono.sinfondo_admin.png",
    "site_logo": "images/fwd/icono.sinfondo_admin_site_logo.png",
    "welcome_sign": "ELANEL",
    # "hide_apps": ["auth"],
    "site_brand": "Administración",
    "custom_css": "css/admin.css",
    "custom_js": "js/admin.js"
}

# JAZZMIN_UI_TWEAKS = {
    
#     # "theme": "flatly",
# }
# CSRF_COOKIE_SECURE =True
CSRF_TRUSTED_ORIGINS = ['https://*.elanelsys.com/','https://elanelsys.com/']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'elanel_web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates/")],
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

WSGI_APPLICATION = 'elanel_web.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}
# DATABASES = {
#    'default': {
#        'ENGINE': os.environ.get('ENGINE'),
#        'NAME': os.environ.get('NAME'),
#        'USER': os.environ.get('USER'),
#        'PASSWORD': os.environ.get('PASSWORD'),
#        'HOST':os.environ.get('HOST'),
#        'PORT':os.environ.get('PORT'),
#    }
# }
DATABASES ={
	'default':{
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': 'elanelweb',
		'USER': 'postgres',
		'PASSWORD': 'klf781CL',
		'HOST': 'localhost',
		'PORT': '5432',
	}
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL =  '/media/'
MEDIA_ROOT = BASE_DIR / "media"
STATICFILES_DIRS = (os.path.join(BASE_DIR,"static"),)
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles/')
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
