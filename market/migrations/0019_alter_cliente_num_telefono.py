# Generated by Django 4.0.6 on 2023-03-02 00:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0018_rename_tamaño_post_tamano'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='num_telefono',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('^\\d+(\\.\\d+)?$', 'Ingrese un número válido')]),
        ),
    ]
