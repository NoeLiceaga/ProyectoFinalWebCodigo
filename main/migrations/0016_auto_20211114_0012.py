# Generated by Django 3.1.5 on 2021-11-14 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_remove_cv_nombres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='empleo_anterior2_fin',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='empleo_anterior_fin',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='foto',
            field=models.ImageField(null=True, upload_to='candidatos/'),
        ),
    ]
