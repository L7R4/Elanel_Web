bind = "0.0.0.0:8000"
module = "elanel_web.wsgi:application"

workers = 4  # Adjust based on your server's resources
worker_connections = 1000
threads = 4

certfile = "/etc/letsencrypt/live/elanelsys.com/fullchain.pem"
keyfile = "/etc/letsencrypt/live/elanelsys.com/privkey.pem"