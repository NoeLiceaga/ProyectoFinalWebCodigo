# Generated by Django 3.1.5 on 2021-11-17 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_ofertadeempleo_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
            ],
        ),
    ]