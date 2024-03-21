from .settings import *

# Recupera la cadena de la variable de entorno
allowed_hosts_str = os.environ.get('ALLOWED_HOSTS')

# Convierte la cadena en una lista separada por comas
ALLOWED_HOSTS = allowed_hosts_str.split(",") if allowed_hosts_str else []

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG =os.environ.get("DEBUG_P")

DATABASES ={
	'default':{
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': os.environ.get('DB_NAME'),
		'USER': os.environ.get('DB_USER'),
		'PASSWORD': os.environ.get('DB_PASS'),
		'HOST': os.environ.get('DB_HOST'),
		'PORT': os.environ.get('DB_PORT'),
	}
}

# Recupera la cadena de la variable de entorno
csrf_trusted_origins_str = os.environ.get('CSRF_TRUSTED_ORIGINS')

# Convierte la cadena en una lista separada por comas
CSRF_TRUSTED_ORIGINS = csrf_trusted_origins_str.split(",") if csrf_trusted_origins_str else []

