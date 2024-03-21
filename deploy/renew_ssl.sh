#!/bin/bash

# Ejecuta el comando de renovación de Certbot
docker-compose -f /path/to/your/docker-compose.prod.yml run --rm certbot -q renew --webroot --webroot-path=/var/www/certbot


# Reinicia los contenedores para cargar los nuevos certificados
docker-compose -f /path/to/your/docker-compose.prod.yml restart