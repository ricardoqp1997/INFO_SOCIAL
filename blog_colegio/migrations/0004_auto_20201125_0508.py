# Generated by Django 3.1.3 on 2020-11-25 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_colegio', '0003_auto_20201125_0506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcolegio',
            name='imagen_contenido',
            field=models.ImageField(null=True, upload_to='blog/imagenes-de-contenido/', verbose_name='Imagen adicional de publicación'),
        ),
    ]