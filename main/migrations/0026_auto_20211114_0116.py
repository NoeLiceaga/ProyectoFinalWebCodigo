# Generated by Django 3.1.5 on 2021-11-14 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_remove_cv_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='foto',
            field=models.ImageField(null=True, upload_to='candidatos/', verbose_name='imagen'),
        ),
        migrations.AlterField(
            model_name='cv',
            name='empleo_anterior_fin',
            field=models.DateField(null=True, verbose_name='Fin'),
        ),
        migrations.AlterField(
            model_name='cv',
            name='empleo_anterior_inicio',
            field=models.DateField(null=True, verbose_name='Inicio'),
        ),
    ]
