from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0028_cuadrocobertura_coberturapack'),
    ]

    operations = [
        migrations.AddField(
            model_name='moto',
            name='destacado',
            field=models.BooleanField(default=False, help_text='Aparece primero en «Destacados de este mes» del inicio.'),
        ),
        migrations.AddField(
            model_name='electrodomestico',
            name='destacado',
            field=models.BooleanField(default=False, help_text='Aparece primero en «Destacados de este mes» del inicio.'),
        ),
    ]
