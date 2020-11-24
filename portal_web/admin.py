from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

# Register your models here.


class CursoAdmin(admin.ModelAdmin):

    list_display = ['grado', 'get_numero_estudiantes', ]
    list_filter = ['grado', ]

    def get_numero_estudiantes(self, obj):
        return Estudiante.objects.filter(curso_id=obj.id).count()

    get_numero_estudiantes.short_description = 'Número de estudiantes inscritos'


class DocenteAdmin(admin.ModelAdmin):

    list_display = ['get_nombre_docente', 'get_numero_asignaturas', 'get_correo_docente', 'contacto', 'whatsapp', ]
    list_filter = ['user__email', 'contacto', ]

    def get_nombre_docente(self, obj):
        return User.objects.get(id=obj.user_id).get_full_name()

    get_nombre_docente.short_description = 'Nombre del docente'

    def get_correo_docente(self, obj):
        return User.objects.get(id=obj.user_id).email

    get_correo_docente.short_description = 'Correo electrónico'

    def get_numero_asignaturas(self, obj):
        return Asignatura.objects.filter(docente_id=obj.id).count()

    get_numero_asignaturas.short_description = 'Número de asignaturas asignadas'


class AsignaturaAdmin(admin.ModelAdmin):

    list_display = ['nombre', 'get_curso_asignado', 'get_nombre_docente', ]
    list_filter = ['nombre', 'docente', ]

    def get_nombre_docente(self, obj):
        return User.objects.get(docente__asignatura=obj.docente_id).get_full_name()

    get_nombre_docente.short_description = 'Docente responsable'

    def get_curso_asignado(self, obj):
        return ',\n'.join([c.get_grado_display() for c in obj.curso.all()])

    get_curso_asignado.short_description = 'Curso/Grado'


class EstudianteAdmin(admin.ModelAdmin):

    list_display = ['get_nombre_estudiante', 'get_curso_estudiante', 'get_asignaturas_estudiante', ]

    def get_nombre_estudiante(self, obj):
        return User.objects.get(id=obj.user_id).get_full_name()

    get_nombre_estudiante.short_description = 'Nombre del estudiante'

    def get_curso_estudiante(self, obj):
        return Curso.objects.get(estudiante=obj).get_grado_display()

    get_curso_estudiante.short_description = 'Grado que cursa'

    def get_asignaturas_estudiante(self, obj):
        return ',\n'.join([c.nombre for c in obj.curso.asignatura_set.all()])

    get_asignaturas_estudiante.short_description = 'Asignaturas provistas'


class TareaAdmin(admin.ModelAdmin):

    add_fieldsets = (
        (
            'Para iniciar la creación de la tarea, indique a que curso pertenece. Luego de eso puede presionar '
            '"guardar y continuar editando" o simplemente "guardar" si desea continuar la edición después.', {
                'classes': ['wide', ],
                'fields': ['curso', ]
            }
        ),
    )

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)


admin.site.register(Curso, CursoAdmin)
admin.site.register(Docente, DocenteAdmin)
admin.site.register(Asignatura, AsignaturaAdmin)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Tarea, TareaAdmin)
