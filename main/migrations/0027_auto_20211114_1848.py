# Generated by Django 3.1.5 on 2021-11-15 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20211114_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ofertadeempleo',
            name='descripcion',
            field=models.CharField(default='any', max_length=1000),
        ),
        migrations.AlterField(
            model_name='ofertadeempleo',
            name='titulo',
            field=models.CharField(max_length=50),
        ),
    ]