from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Curso(models.Model):

    class CursosSitio(models.TextChoices):

        PRIMERO = '1', _('Primero')
        SEGUNDO = '2', _('Segundo')
        TERCERO = '3', _('Tercero')
        CUARTO = '4', _('Cuarto')
        QUINTO = '5', _('Quinto')
        SEXTO = '6', _('Sexto')
        SEPTIMO = '7', _('Septimo')
        OCTAVO = '8', _('Octavo')
        NOVENO = '9', _('Noveno')
        DECIMO = '10', _('Decimo')
        UNDECIMO = '11', _('Undecimo')

    grado = models.CharField(
        choices=CursosSitio.choices,
        verbose_name='Grado',
        help_text='Especifique el grado de este curso',
        unique=True,
        max_length=2,
    )

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.get_grado_display()


class Docente(models.Model):

    WHATSAPP_CHOICES = [
        (True, 'WhatsApp disponible'),
        (False, 'WhatsApp no disponible'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Usuario',
        help_text='Indique a que usuario de este sitio le corresponde este tipo de cuenta'
    )
    contacto = models.CharField(
        verbose_name='Número telefónico de contacto',
        help_text='Ingrese el número de contacto de este docente',
        unique=True,
        null=True,
        max_length=10,
    )
    whatsapp = models.BooleanField(
        verbose_name='Disponibilidad para WhatsApp',
        help_text='Indique si este docente tiene disponibilidad de ser conectado a través de WhatsApp',
        choices=WHATSAPP_CHOICES,
        default=True,
    )

    class Meta:
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'

    def __str__(self):
        return self.user.get_full_name()


class Asignatura(models.Model):

    docente = models.ForeignKey(
        Docente,
        on_delete=models.SET_NULL,
        verbose_name='Docente responsable',
        help_text='Especifique quien es el docente asignado para esta asignatura',
        null=True
    )
    curso = models.ManyToManyField(
        Curso,
        verbose_name='Curso de la asignatura',
        help_text='Asigne el grado a la que esta asignatura iría orientada',
    )
    nombre = models.CharField(
        verbose_name='Nombre de la asignatura',
        help_text='Indique el nombre de la asignatura a registrar',
        max_length=100,
        unique=True
    )

    class Meta:
        verbose_name = 'Asignatura'
        verbose_name_plural = 'Asignaturas'

    def __str__(self):
        return self.nombre


class Estudiante(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Usuario',
        help_text='Indique a que usuario de este sitio le corresponde este tipo de cuenta'
    )
    curso = models.ForeignKey(
        Curso,
        verbose_name='Curso del alumno',
        help_text='Asigne el grado al que pertenece este alumno',
        on_delete=models.SET_NULL,
        null=True
    )
    whatsapp = models.CharField(
        verbose_name='Número telefónico de Whatsapp',
        help_text='Ingrese el número de contacto de este estudiante, también servirá para contacto por WhatsApp.\n'
                  'NOTA: En caso de que el estudiante no posea este tipo de contacto agregar el del acudiente.',
        unique=True,
        null=True,
        max_length=10,
    )
    direccion = models.CharField(
        verbose_name='Dirección de domicilio',
        help_text='Indique la dirección de domicilio de este estudiante. En dado caso de que se requiera esta '
                  'información para temas academicos con sus compañeros, docentes o administrativos de la '
                  'institución.',
        max_length=255,
        null=True,
    )

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'

    def __str__(self):
        return self.user.get_full_name()


class Tarea(models.Model):

    EN_DESARROLLO = 'DES'
    ENVIADA = 'ENV'
    REALIZADA = 'REA'
    CALIFICADA = 'CLF'

    REGIMEN_CHOICES = [
        (EN_DESARROLLO, 'En desarrollo'),
        (ENVIADA, 'Enviada'),
        (REALIZADA, 'Realizada'),
        (CALIFICADA, 'Calificada'),
    ]

    estado = models.CharField(
        choices=REGIMEN_CHOICES,
        default='DES',
        max_length=3,
        verbose_name='Estado de la tarea',
    )
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        verbose_name='Curso o grado',
        help_text='Especifique a que grupo de estudiantes de un grado determinado será esta tarea.'
    )
    asignatura = models.ForeignKey(
        Asignatura,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Asignatura de la tarea',
        help_text='Es necesario también determinar a que asignatura está dirigida esta tarea (en caso de que'
                  'usted dicte mas de una asignatura en un mismo curso).'
    )
    estudiante = models.ManyToManyField(
        Estudiante,
        verbose_name='Estudiante(s)',
        help_text='Indique el o los estudiantes del curso que requieran hacer esta tarea.',

    )

    titulo = models.CharField(
        verbose_name='Título de la tarea',
        help_text='Asigne el título para esta tarea, sea lo mas específico posible para que los estudiantes'
                  'tengan claro el objetivo de la tarea.',
        max_length=100,
        null=True,
    )
    descripcion = models.TextField(
        verbose_name='Descripción o contenido',
        help_text='Desrciba el compromiso que sus estudiantes tiene que hacer, trate de ser puntual para aminorar'
                  'las dudas de sus estudiantes.',
        max_length=500,
        null=True,
    )
    adjuntos = models.FileField(
        verbose_name='Archivos adjuntos',
        help_text='(Opcional). Si se requiere para el desarrollo de la tarea, adjunte documentos o multimedia'
                  'para el desarrollo de la tarea.',
        null=True,
        blank=True,
        upload_to='tareas/'
    )

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'

    def __str__(self):

        if self.titulo is None:
            return str(self.curso.get_grado_display()) + ' - Tarea sin especificar'
        else:
            return str(self.curso.get_grado_display()) + ' - ' + self.titulo


class Clase(models.Model):

    INACTIVA = False
    ACTIVA = True

    REGIMEN_CHOICES = [
        (INACTIVA, 'Clase inactiva'),
        (ACTIVA, 'Clase activa'),
    ]

    estado = models.BooleanField(
        choices=REGIMEN_CHOICES,
        default=False,
        verbose_name='Estado de la clase',
    )

    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        verbose_name='Curso o grado',
        help_text='Especifique a que grupo de estudiantes de un grado determinado será esta clase.'
    )
    asignatura = models.ForeignKey(
        Asignatura,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Asignatura de la tarea',
        help_text='Es necesario también determinar a que asignatura está dirigida esta clase (en caso de que'
                  'usted dicte mas de una asignatura en un mismo curso).'
    )
    estudiante = models.ManyToManyField(
        Estudiante,
        verbose_name='Estudiante(s)',
        help_text='Indique el o los estudiantes del curso que recibirán esta clase.',

    )

    titulo = models.CharField(
        verbose_name='Título de la clase',
        help_text='Asigne el título para el contenido desarrollado de esta clase',
        max_length=100,
        null=True,
    )
    descripcion = models.TextField(
        verbose_name='Descripción o contenido',
        help_text='Desrciba claramente el contenido de esta clase, puntualice lo que el estudiante encontrará en '
                  'este tema, para luego complementarlo con los archivos adjuntos requeridos',
        max_length=500,
        null=True,
    )
    adjuntos = models.FileField(
        verbose_name='Archivos adjuntos',
        help_text='Es recomendable dejar contenidos adjuntos como documentos, imagenes, etc para que el estudiante'
                  'pueda instruirse sin inconvenientes.',
        null=True,
        blank=True,
        upload_to='clases/'
    )

    class Meta:
        verbose_name = 'Clase'
        verbose_name_plural = 'Clases'

    def __str__(self):

        if self.titulo is None:
            return str(self.curso.get_grado_display()) + ' - Clase sin especificar'
        else:
            return str(self.curso.get_grado_display()) + ' - ' + self.titulo
