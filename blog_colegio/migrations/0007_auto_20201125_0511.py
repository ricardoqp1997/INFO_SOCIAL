# Generated by Django 3.1.3 on 2020-11-25 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_colegio', '0006_auto_20201125_0510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcolegio',
            name='imagen_contenido',
            field=models.ImageField(blank=True, null=True, upload_to='blog/imagenes-de-contenido/', verbose_name='Imagen adicional de publicación'),
        ),
        migrations.AlterField(
            model_name='blogcolegio',
            name='youtube_link',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Link de Youtube'),
        ),
    ]
