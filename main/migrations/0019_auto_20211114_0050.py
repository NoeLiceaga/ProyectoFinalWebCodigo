# Generated by Django 3.1.5 on 2021-11-14 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20211114_0046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cv',
            name='curp',
        ),
        migrations.AddField(
            model_name='cv',
            name='id_usuario',
            field=models.CharField(max_length=50, null=True),
        ),
    ]