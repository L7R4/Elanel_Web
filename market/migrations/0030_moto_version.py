from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0029_moto_destacado_electrodomestico_destacado'),
    ]

    operations = [
        migrations.AddField(
            model_name='moto',
            name='version',
            field=models.CharField(blank=True, choices=[('base', 'Base'), ('full', 'Full')], default='', help_text='Solo para los modelos que se venden en versión Base y Full. Se muestra como etiqueta en la tarjeta.', max_length=4, verbose_name='Versión'),
        ),
    ]
