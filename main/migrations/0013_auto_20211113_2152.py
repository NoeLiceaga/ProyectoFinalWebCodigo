# Generated by Django 3.1.5 on 2021-11-14 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20211113_2037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cv',
            name='apellido_materno',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='apellido_paterno',
        ),
        migrations.AddField(
            model_name='cv',
            name='apellido',
            field=models.CharField(default='Apellido', max_length=100),
        ),
        migrations.AlterField(
            model_name='cv',
            name='sexo',
            field=models.CharField(choices=[('1', 'Cualquiera'), ('2', 'Masculino'), ('3', 'Femenino')], default=1, max_length=15),
        ),
    ]
