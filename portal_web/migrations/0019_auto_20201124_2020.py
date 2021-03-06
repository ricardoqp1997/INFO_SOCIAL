# Generated by Django 3.1.3 on 2020-11-25 01:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portal_web', '0018_estudiante_direccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='clase',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de publicación'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarea',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de publicación'),
            preserve_default=False,
        ),
    ]
