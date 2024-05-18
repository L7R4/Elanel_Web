from .settings import *
ALLOWED_HOST = ["*"]
SECRET_KEY = "development_key"
DEBUG = True


DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': BASE_DIR / 'db.sqlite3',
   }
}