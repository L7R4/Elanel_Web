from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Cliente,Personal
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

def create_email(email, subject, template_path,context):
    template = get_template(template_path)
    content = template.render(context)
    mail = EmailMultiAlternatives(
        subject=subject,
        body='',
        from_email=settings.EMAIL_HOST_USER,
        to = [email],
    )
    mail.attach_alternative(content, "text/html")
    mail.fail_silently = False
    return mail

@receiver(post_save, sender=Cliente)
def enviar_correo(sender, instance, created, **kwargs):
    if created:  # Solo se envía el correo si se crea un objeto nuevo
        mail = create_email(
            'lautaro.rodriguez553@gmail.com',
            instance.objetivo,
            "mail.html",
            {
                "person": instance.nombre_completo,
                "target": instance.objetivo,
                "num_tel": instance.num_telefono,
                "correo" : instance.email,
                "provincia": instance.provincia
            }
            )
        mail.send()
        print("Se envio el correo")


@receiver(post_save, sender=Personal)
def enviar_correo_personal(sender, instance, created, **kwargs):
    if created:  # Solo se envía el correo si se crea un objeto nuevo
        mail = create_email(
            'lautaro.rodriguez553@gmail.com',
            instance.cv,
            "mail.html",
            {
                "person": instance.nombre_completo,
                "cv": instance.cv,
                "num_tel": instance.num_telefono,
                "correo" : instance.email
            }
            )
        archivo = open(str(settings.MEDIA_ROOT)+"/"+str(instance.cv), 'rb')
        mail.attach(str(settings.MEDIA_ROOT)+"/"+str(instance.cv),archivo.read(),"application/pdf")
        
        mail.send()
        print("Se envio el correo")