# Generated by Django 3.1.3 on 2020-11-24 01:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Indique el nombre de la asignatura a registrar', max_length=100, unique=True, verbose_name='Nombre de la asignatura')),
            ],
            options={
                'verbose_name': 'Asignatura',
                'verbose_name_plural': 'Asignaturas',
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grado', models.CharField(choices=[('1', 'Primero'), ('2', 'Segundo'), ('3', 'Tercero'), ('4', 'Cuarto'), ('5', 'Quinto'), ('6', 'Sexto'), ('7', 'Septimo'), ('8', 'Octavo'), ('9', 'Noveno'), ('10', 'Decimo'), ('11', 'Undecimo')], help_text='Especifique el grado de este curso', max_length=2, unique=True, verbose_name='Grado')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.ForeignKey(help_text='Asigne el grado al que pertenece este alumno', null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal_web.curso', verbose_name='Curso del alumno')),
                ('user', models.OneToOneField(help_text='Indique a que usuario de este sitio le corresponde este tipo de cuenta', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Estudiante',
                'verbose_name_plural': 'Estudiantes',
            },
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, help_text='Asigne el título para esta tarea, sea lo mas específico posible para que los estudiantestengan claro el objetivo de la tarea.', max_length=100, verbose_name='Título de la tarea')),
                ('descripcion', models.TextField(blank=True, help_text='Desrciba el compromiso que sus estudiantes tiene que hacer, trate de ser puntual para aminorarlas dudas de sus estudiantes.', max_length=500, verbose_name='Descripción/contenido')),
                ('asignatura', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal_web.asignatura')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal_web.curso')),
                ('estudiante', models.ManyToManyField(to='portal_web.Estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contacto', models.CharField(help_text='Ingrese el número de contacto de este docente', max_length=10, null=True, unique=True, verbose_name='Número telefónico de contacto')),
                ('whatsapp', models.BooleanField(choices=[(True, 'WhatsApp disponible'), (False, 'WhatsApp no disponible')], default=True, help_text='Indique si este docente tiene disponibilidad de ser conectado a través de WhatsApp', verbose_name='Disponibilidad para WhatsApp')),
                ('user', models.OneToOneField(help_text='Indique a que usuario de este sitio le corresponde este tipo de cuenta', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Docente',
                'verbose_name_plural': 'Docentes',
            },
        ),
        migrations.AddField(
            model_name='asignatura',
            name='curso',
            field=models.ManyToManyField(help_text='Asigne el grado a la que esta asignatura iría orientada', to='portal_web.Curso', verbose_name='Curso de la asignatura'),
        ),
        migrations.AddField(
            model_name='asignatura',
            name='docente',
            field=models.ForeignKey(help_text='Especifique quien es el docente asignado para esta asignatura', null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal_web.docente', verbose_name='Docente responsable'),
        ),
    ]
