# Generated by Django 3.1.3 on 2020-11-25 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_colegio', '0005_blogcolegio_fecha_publicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcolegio',
            name='titulo',
            field=models.CharField(default='Post', max_length=100, verbose_name='Título de la publicación'),
        ),
    ]
