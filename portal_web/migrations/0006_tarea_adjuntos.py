# Generated by Django 3.1.3 on 2020-11-24 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal_web', '0005_auto_20201124_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='adjuntos',
            field=models.FileField(help_text='(Opcional). Si se requiere para el desarrollo de la tarea, adjunte documentos o multimediapara el desarrollo de la tarea.', null=True, upload_to='', verbose_name='Archivos adjuntos'),
        ),
    ]