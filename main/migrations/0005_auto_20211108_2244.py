# Generated by Django 3.1.5 on 2021-11-09 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20211108_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='categoria_principal',
            field=models.CharField(max_length=100, null=True),
        ),
    ]