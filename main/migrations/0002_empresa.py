# Generated by Django 3.1.5 on 2021-11-07 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to='empresa')),
                ('direccion', models.CharField(max_length=300)),
                ('telefono', models.IntegerField(max_length=10)),
            ],
        ),
    ]
