# Generated by Django 3.1.3 on 2020-11-25 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_colegio', '0008_blogcolegio_contenido'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcolegio',
            name='contenido_add',
            field=models.TextField(default='Contenido adicional', max_length=600, verbose_name='Contenido adicional para la publicación'),
        ),
    ]