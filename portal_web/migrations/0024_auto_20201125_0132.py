# Generated by Django 3.1.3 on 2020-11-25 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal_web', '0023_auto_20201125_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soluciontarea',
            name='estudiante',
            field=models.ForeignKey(help_text='Corresponde al usuario que desarrolla, desarrolló, o desarrollará la taréa correspondiente', on_delete=django.db.models.deletion.CASCADE, to='portal_web.estudiante', verbose_name='Estudiante que desarrolla la tarea'),
        ),
    ]
