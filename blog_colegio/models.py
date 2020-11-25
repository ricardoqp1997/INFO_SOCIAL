from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class BlogColegio(models.Model):

    fecha_publicacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de publicación'
    )

    autor = models.ForeignKey(
        User,
        verbose_name='Autor de la publicación',
        on_delete=models.CASCADE
    )

    titulo = models.CharField(
        verbose_name='Título de la publicación',
        max_length=100,
        default='Post'
    )

    contenido = models.TextField(
        verbose_name='Contenido de la publicación',
        max_length=600,
        default='Contenido'
    )

    portada = models.ImageField(
        verbose_name='Portada de la publicación',
        upload_to='blog/portadas/',
        blank=True
    )

    imagen_contenido = models.ImageField(
        verbose_name='Imagen adicional de publicación',
        null=True,
        blank=True,
        upload_to='blog/imagenes-de-contenido/'
    )

    contenido_add = models.TextField(
        verbose_name='Contenido adicional para la publicación',
        max_length=600,
        null=True,
        blank=True,
    )

    youtube_link = models.CharField(
        verbose_name='Link de Youtube',
        null=True,
        blank=True,
        max_length=255,
    )

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

    def __str__(self):
        return self.titulo
