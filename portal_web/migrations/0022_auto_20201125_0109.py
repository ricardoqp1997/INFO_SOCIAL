# Generated by Django 3.1.3 on 2020-11-25 06:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portal_web', '0021_auto_20201125_0048'),
    ]

    operations = [
        migrations.AddField(
            model_name='soluciontarea',
            name='estado',
            field=models.BooleanField(choices=[('SINREV', 'Tarea sin revisar'), ('ENVIAD', 'Tarea enviada'), ('REVISD', 'Tarea calificada')], default=False, verbose_name='Estado de resolución de la tarea'),
        ),
        migrations.AddField(
            model_name='soluciontarea',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de resolución'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='soluciontarea',
            name='revision',
            field=models.CharField(help_text='Calificación final de la tarea resuelta', max_length=5, null=True, verbose_name='Revisión de la tarea'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='estado',
            field=models.CharField(choices=[('DES', 'En desarrollo'), ('ENV', 'Enviada y asignada')], default='DES', max_length=3, verbose_name='Estado de la tarea'),
        ),
    ]
