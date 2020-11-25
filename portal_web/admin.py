from django.contrib import admin
from .models import *
from .forms import *
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
        return User.objects.get(id=Docente.objects.get(id=obj.docente_id).user_id).get_full_name()

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

    form = AssigmentForm

    list_display = ['get_nombre_tarea', 'get_asignatura_asignada', 'estado', ]
    list_filter = ['asignatura__docente', 'curso', 'asignatura', 'estudiante', ]

    add_fieldsets = (
        (
            'Para iniciar la creación de la tarea, indique a que curso pertenece y a que asignatura corresponde. '
            'Luego de eso puede presionar "guardar y continuar editando" o simplemente "guardar" si desea continuar '
            'la edición después.', {
                'classes': ['wide', 'extrapretty', ],
                'fields': ['curso', ]
            }
        ),
    )

    fieldsets = (
        (
            None, {
                'classes': ['wide', 'extrapretty', ],
                'fields': ['fecha_creacion', 'estado', ]
            }
        ),
        (
            'Curso o grado a quien estará enfocada esta tarea o entregable.', {
                'classes': ['wide', 'extrapretty', ],
                'fields': ['curso', ]
            }
        ),
        (
            'Ingrese información mas especifica sobre la asignatura y a que estudiante o estudiantes estará dirigido'
            'este entregable.', {
                'classes': ['wide', 'extrapretty', ],
                'fields': ['asignatura', 'estudiante', ]
            }
        ),
        (
            'Personalice su tarea con los siguientes campos.'
            'este entregable.', {
                'classes': ['wide', 'extrapretty', ],
                'fields': ['titulo', 'descripcion', 'adjuntos', ]
            }
        ),
    )

    readonly_fields = ['fecha_creacion', 'estado', ]

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == 'asignatura':
            kwargs["queryset"] = Asignatura.objects.filter(
                docente_id=Docente.objects.get(
                    user_id=request.user.id
                )
            ).distinct()

        if db_field.name == 'curso':
            kwargs["queryset"] = Curso.objects.filter(
                asignatura__docente=Docente.objects.get(
                    user_id=request.user.id
                ).id
            ).distinct()

        return super(TareaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'estudiante':
            kwargs["queryset"] = Estudiante.objects.filter(
                curso__asignatura__docente=Docente.objects.get(
                    user_id=request.user.id
                ).id
            ).distinct()

        return super(TareaAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):

        if (obj.titulo is not None) or (obj.descripcion is not None):
            print('hola mundo')
            obj.estado = Tarea.ENVIADA

        super(TareaAdmin, self).save_model(request, obj, form, change)

    def get_nombre_tarea(self, obj):
        if obj.titulo is None:
            return str(obj.curso.get_grado_display()) + ' - Tarea sin especificar'
        else:
            return str(obj.curso.get_grado_display()) + ' - ' + obj.titulo

    get_nombre_tarea.short_description = 'Tarea'

    def get_asignatura_asignada(self, obj):
        return Asignatura.objects.get(nombre=obj.asignatura).nombre

    get_asignatura_asignada.short_description = 'Asignatura de la tarea'


class ClaseAdmin(admin.ModelAdmin):

    form = AssigmentForm

    list_display = ['get_nombre_tarea', 'get_asignatura_asignada', 'get_datos_adjuntos_validate', ]
    list_filter = ['asignatura__docente', 'curso', 'asignatura', 'estudiante', ]

    add_fieldsets = (
        (
            'Para iniciar la creación de la clase, indique a que curso pertenece y a que asignatura corresponde. '
            'Luego de eso puede presionar "guardar y continuar editando" o simplemente "guardar" si desea continuar '
            'la edición después.', {
                'classes': ['wide', 'extrapretty', ],
                'fields': ['curso', ]
            }
        ),
    )

    fieldsets = (
        (
            None, {
                'classes': ['wide', 'extrapretty', ],
                'fields': ['fecha_creacion', 'estado', ]
            }
        ),
        (
            'Curso o grado a quien estará enfocada esta clase o contenido.', {
                'classes': ['wide', 'extrapretty', ],
                'fields': ['curso', ]
            }
        ),
        (
            'Ingrese información mas especifica sobre la asignatura y a que estudiante o estudiantes estará dirigido'
            'este entregable.', {
                'classes': ['wide', 'extrapretty', ],
                'fields': ['asignatura', 'estudiante', ]
            }
        ),
        (
            'Personalice su clase con los siguientes campos.'
            'este entregable.', {
                'classes': ['wide', 'extrapretty', ],
                'fields': ['titulo', 'descripcion', 'adjuntos', ]
            }
        ),
    )

    readonly_fields = ['fecha_creacion', 'estado', ]

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == 'asignatura':
            kwargs["queryset"] = Asignatura.objects.filter(
                docente_id=Docente.objects.get(
                    user_id=request.user.id
                ).id
            ).distinct()

        if db_field.name == 'curso':
            kwargs["queryset"] = Curso.objects.filter(
                asignatura__docente=Docente.objects.get(
                    user_id=request.user.id
                ).id
            ).distinct()

        return super(ClaseAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'estudiante':
            kwargs["queryset"] = Estudiante.objects.filter(
                curso__asignatura__docente=Docente.objects.get(
                    user_id=request.user.id
                ).id
            ).distinct()

        return super(ClaseAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):

        if (obj.titulo is not None) or (obj.descripcion is not None):
            print('hola mundo')
            obj.estado = Clase.ACTIVA

        super(ClaseAdmin, self).save_model(request, obj, form, change)

    def get_nombre_tarea(self, obj):
        if obj.titulo is None:
            return str(obj.curso.get_grado_display()) + ' - Clase sin especificar'
        else:
            return str(obj.curso.get_grado_display()) + ' - ' + obj.titulo

    get_nombre_tarea.short_description = 'Clase'

    def get_asignatura_asignada(self, obj):
        return Asignatura.objects.get(nombre=obj.asignatura).nombre

    get_asignatura_asignada.short_description = 'Asignatura de la Clase'

    def get_datos_adjuntos_validate(self, obj):
        if obj.adjuntos:
            return True
        else:
            return False

    get_datos_adjuntos_validate.short_description = '¿Archivos adjuntos?'
    get_datos_adjuntos_validate.boolean = True


admin.site.register(Curso, CursoAdmin)
admin.site.register(Docente, DocenteAdmin)
admin.site.register(Asignatura, AsignaturaAdmin)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Tarea, TareaAdmin)
admin.site.register(Clase, ClaseAdmin)
