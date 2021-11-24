# Generated by Django 3.1.5 on 2021-11-14 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20211113_2152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cv',
            name='apellido',
        ),
        migrations.AlterField(
            model_name='cv',
            name='nombres',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='sexo',
            field=models.CharField(choices=[('1', 'Cualquiera'), ('2', 'Masculino'), ('3', 'Femenino')], default=1, max_length=15, null=True),
        ),
    ]