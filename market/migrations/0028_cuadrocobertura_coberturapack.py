from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0027_alter_post_postimage_celular_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CuadroCobertura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=20, verbose_name='Versión')),
                ('vigente_desde', models.DateField(verbose_name='Vigente desde')),
                ('archivo', models.FileField(blank=True, null=True, upload_to='cobertura/', verbose_name='PDF del cuadro')),
                ('publicado', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Cuadro de cobertura',
                'verbose_name_plural': 'Cuadros de cobertura',
                'ordering': ['-vigente_desde'],
            },
        ),
        migrations.CreateModel(
            name='CoberturaPack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pack', models.CharField(choices=[('Basico', 'Básico'), ('Estandar', 'Estándar'), ('Premium', 'Premium')], max_length=10)),
                ('servicios_anuales', models.PositiveSmallIntegerField()),
                ('cobertura_por_servicio', models.DecimalField(decimal_places=2, max_digits=15)),
                ('cuadro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='packs', to='market.cuadrocobertura')),
            ],
            options={
                'verbose_name': 'Pack',
                'verbose_name_plural': 'Packs',
                'ordering': ['servicios_anuales'],
            },
        ),
    ]
