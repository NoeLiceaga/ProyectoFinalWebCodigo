# Generated by Django 3.1.5 on 2021-11-14 07:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0023_remove_cv_id_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='id_usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
