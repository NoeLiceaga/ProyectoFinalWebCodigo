# Generated by Django 3.1.5 on 2021-11-11 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_genero_ofertadeempleo_tipodetrabajo'),
    ]

    operations = [
        migrations.AddField(
            model_name='ofertadeempleo',
            name='descripcion',
            field=models.CharField(default='any', max_length=500),
        ),
    ]
