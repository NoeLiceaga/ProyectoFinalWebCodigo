# Generated by Django 3.1.5 on 2021-11-17 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_auto_20211116_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pruebapostulante',
            name='estado',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='main.estado'),
        ),
    ]
