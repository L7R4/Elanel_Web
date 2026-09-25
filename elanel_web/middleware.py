from django.shortcuts import render
from django.conf import settings

class MaintenanceMiddleware:
    """
    Middleware que activa el modo mantenimiento para todas las URLs de la página web.
    Permite únicamente la descarga de archivos estáticos y media para mantener el diseño y los recursos.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if getattr(settings, 'MAINTENANCE_MODE', True):
            static_url = getattr(settings, 'STATIC_URL', '/static/')
            media_url = getattr(settings, 'MEDIA_URL', '/media/')

            # Permitir que las solicitudes de archivos estáticos y de media continúen
            if request.path.startswith(static_url) or request.path.startswith(media_url):
                return self.get_response(request)

            response = render(request, 'mantenimiento.html', status=503)
            response['Retry-After'] = '3600'
            return response

        return self.get_response(request)
