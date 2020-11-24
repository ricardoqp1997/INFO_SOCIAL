# Generated by Django 3.1.3 on 2020-11-24 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal_web', '0002_tarea'),
    ]

    operations = [
        migrations.CreateModel(
            name='TareaAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='tarea',
            name='descripcion',
            field=models.TextField(blank=True, help_text='Desrciba el compromiso que sus estudiantes tiene que hacer, trate de ser puntual para aminorarlas dudas de sus estudiantes.', max_length=500, verbose_name='Descripción/contenido'),
        ),
        migrations.AddField(
            model_name='tarea',
            name='titulo',
            field=models.CharField(blank=True, help_text='Asigne el título para esta tarea, sea lo mas específico posible para que los estudiantestengan claro el objetivo de la tarea.', max_length=100, verbose_name='Título de la tarea'),
        ),
    ]