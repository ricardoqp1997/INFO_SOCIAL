# Generated by Django 3.1.3 on 2020-11-25 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal_web', '0024_auto_20201125_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soluciontarea',
            name='tarea',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='portal_web.tarea', verbose_name='Tarea Desarrollada'),
        ),
    ]
