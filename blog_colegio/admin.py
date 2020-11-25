from django.contrib import admin
from .models import BlogColegio


class BlogAdmin(admin.ModelAdmin):

    list_display = ['titulo', 'autor', 'fecha_publicacion', ]
    list_filter = list_display

    fieldsets = (
        (
            'Información de la publicación', {
                'classes': ['wide', 'extrapretty', ],
                'fields': ['fecha_publicacion', 'autor', ]
            }
        ),
        (
            'Contenido de la publicación', {
                'classes': ['wide', 'extrapretty', ],
                'fields': ['portada', 'titulo', 'contenido', ]
            }
        ),
        (
            'Elementos adicionales para la publicación', {
                'classes': ['wide', 'extrapretty', ],
                'fields': ['imagen_contenido', 'contenido_add', 'youtube_link', ]
            }
        ),
    )

    readonly_fields = ['fecha_publicacion', ]

    def save_model(self, request, obj, form, change):
        if obj.youtube_link is not None:
            obj.youtube_link = obj.youtube_link.replace('watch?v=', 'embed/')
        return super(BlogAdmin, self).save_model(request, obj, form, change)


admin.site.register(BlogColegio, BlogAdmin)
