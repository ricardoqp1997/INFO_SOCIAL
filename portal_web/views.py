# Librerías de Django para el manejo de las vistas, plantillas y navegación
# Módulos de configuracion del proyecto
from django.conf import settings
# Módulos para la manipulación de usuarios
from django.contrib.auth import (
    authenticate,
    login,
    logout
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)

# Módulos de forms.py
from .forms import (
    UserLoginForm,
    AssigmentResolution
)
from .models import *

user = None


# redireccionamiento de la pagina respecto a la autenticación del usuario
def index(request):
    if request.user.is_authenticated:
        return redirect('/main/')
    else:
        logout(request)
        return redirect('login/')


# redireccionamiento de la pagina al portal administrativo
def redirect_admin(request):
    return redirect('/admin/')


# Vista de inicio de sesión

def login_view(request):

    global user

    form = UserLoginForm(request.POST or None)

    if form.is_valid():

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect('/main/')

    login_context = {
        'form': form,
        'page_title': 'Inicio de sesión',

    }

    return render(request, 'login.html', login_context)


# Vista de acceso a portal principal (Hola mundo en primer prueba)

@login_required(login_url=settings.LOGIN_URL)
def contenido_docente(request):
    return redirect('/admin/')


@login_required(login_url=settings.LOGIN_URL)
def main(request):

    if request.user.is_authenticated:

        global user
        tipo_usuario = Group.objects.get(user=request.user).name
        # print(request.user.username)
        # print('tipo_usuario: ' + str(tipo_usuario))

        context_inicio = {
            'Title': 'Inicio',
            'tipo_usuario': tipo_usuario
        }
        return render(request, 'main.html', context_inicio)
    else:
        return redirect('/login/')


@login_required(login_url=settings.LOGIN_URL)
def contenido_estudiante(request):

    tipo_usuario = Group.objects.get(user=request.user).name

    try:
        asignaturas = Asignatura.objects.filter(curso__estudiante__user_id=request.user)
        cant_asignaturas = asignaturas.count()
    except:
        cant_asignaturas = asignaturas = None

    try:
        tareas = Tarea.objects.filter(
            estudiante__user_id=request.user.id,
            estado=Tarea.ENVIADA
        )
        cant_tareas = tareas.count()
        list_tareas = tareas[:5]
    except:
        list_tareas = cant_tareas = tareas = None

    try:
        clases = Clase.objects.filter(
            estudiante__user_id=request.user.id
        )
        cant_clases = clases.count()
        list_clases = clases[:5]
    except:
        list_clases = cant_clases = clases = None

    context_contenido = {
        'Title': 'Aula de clases',
        'tipo_usuario': tipo_usuario,
        'on_screen': 'tablero',

        'subjects_count': cant_asignaturas,
        'tasks_count': cant_tareas,
        'classes_count': cant_clases,

        'tasks_list': list_tareas,
        'classes_list': list_clases,
    }

    return render(request, 'dashboard.html', context_contenido)


def panel_curso(request):

    tipo_usuario = Group.objects.get(user=request.user).name

    try:
        asignaturas = Asignatura.objects.filter(curso__estudiante__user_id=request.user)
        cant_asignaturas = asignaturas.count()
    except:
        cant_asignaturas = asignaturas = None

    try:
        tareas = Tarea.objects.filter(
            estudiante__user_id=request.user.id,
            estado=Tarea.ENVIADA
        )
        cant_tareas = tareas.count()
        list_tareas = tareas[:5]
    except:
        list_tareas = cant_tareas = tareas = None

    try:
        clases = Clase.objects.filter(
            estudiante__user_id=request.user.id
        )
        cant_clases = clases.count()
        list_clases = clases[:5]
    except:
        list_clases = cant_clases = clases = None

    try:
        partners = Estudiante.objects.filter(
            curso__estudiante__user_id=request.user.id
        ).exclude(clase__estudiante__user_id=request.user.id)
        print(partners)
    except:
        partners = None

    context_contenido = {
        'Title': 'Mi curso',
        'tipo_usuario': tipo_usuario,
        'on_screen': 'curso',

        'subjects_count': cant_asignaturas,
        'tasks_count': cant_tareas,
        'classes_count': cant_clases,

        'tasks_list': list_tareas,
        'classes_list': list_clases,
        'partners_list': partners,
    }

    return render(request, 'curso.html', context_contenido)


def panel_asignaturas(request):

    tipo_usuario = Group.objects.get(user=request.user).name

    try:
        asignaturas = Asignatura.objects.filter(curso__estudiante__user_id=request.user)
        cant_asignaturas = asignaturas.count()
    except:
        cant_asignaturas = asignaturas = None

    try:
        tareas = Tarea.objects.filter(
            estudiante__user_id=request.user.id,
            estado=Tarea.ENVIADA
        )
        cant_tareas = tareas.count()
        list_tareas = tareas[:5]
    except:
        list_tareas = cant_tareas = tareas = None

    try:
        clases = Clase.objects.filter(
            estudiante__user_id=request.user.id
        )
        cant_clases = clases.count()
        list_clases = clases[:5]
    except:
        list_clases = cant_clases = clases = None

    context_contenido = {
        'Title': 'Mis asignaturas',
        'tipo_usuario': tipo_usuario,
        'on_screen': 'asignaturas',

        'subjects_count': cant_asignaturas,
        'tasks_count': cant_tareas,
        'classes_count': cant_clases,

        'tasks_list': list_tareas,
        'classes_list': list_clases,
        'subjects_list': asignaturas,
    }

    return render(request, 'asignaturas.html', context_contenido)


class ListaTareas(ListView):

    paginate_by = 5
    model = Tarea
    template_name = 'tareas.html'
    queryset = Tarea.objects.all()

    def get_queryset(self):
        return Tarea.objects.filter(curso__estudiante__user_id=self.request.user.id)

    def get_context_data(self, **kwargs):

        tipo_usuario = Group.objects.get(user=self.request.user).name

        try:
            asignaturas = Asignatura.objects.filter(curso__estudiante__user_id=self.request.user)
            cant_asignaturas = asignaturas.count()
        except:
            cant_asignaturas = asignaturas = None

        try:
            tareas = Tarea.objects.filter(
                estudiante__user_id=self.request.user.id,
                estado=Tarea.ENVIADA
            )
            cant_tareas = tareas.count()
            list_tareas = tareas[:5]
        except:
            list_tareas = cant_tareas = tareas = None

        try:
            clases = Clase.objects.filter(
                estudiante__user_id=self.request.user.id
            )
            cant_clases = clases.count()
            list_clases = clases[:5]
        except:
            list_clases = cant_clases = clases = None

        context = super(ListaTareas, self).get_context_data(**kwargs)

        context.update(
            {
                'Title': 'Mis tareas',
                'tipo_usuario': tipo_usuario,
                'on_screen': 'tareas_pendientes',

                'subjects_count': cant_asignaturas,
                'tasks_count': cant_tareas,
                'classes_count': cant_clases,

                'tasks_list': list_tareas,
                'classes_list': list_clases,
            }
        )

        return context


class ResolverTareas(CreateView):

    model = SolucionTarea
    queryset = SolucionTarea.objects.all()
    template_name = 'tareas_detalles.html'
    form_class = AssigmentResolution

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.object = None

    def form_valid(self, form):

        form.instance.estudiante = Estudiante.objects.get(user_id=self.request.user)
        form.instance.tarea = Tarea.objects.get(id=self.kwargs.get('assigment_pk'))
        form.instance.estado = SolucionTarea.ENVIADA

        return super(ResolverTareas, self).form_valid(form)

    def get_success_url(self):
        return reverse('vista_tareas_resueltas', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):

        tipo_usuario = Group.objects.get(user=self.request.user).name

        assigment = Tarea.objects.get(id=self.kwargs.get('assigment_pk'))
        student_assigment = Estudiante.objects.get(user_id=self.request.user)

        try:
            asignaturas = Asignatura.objects.filter(curso__estudiante__user_id=self.request.user)
            cant_asignaturas = asignaturas.count()
        except:
            cant_asignaturas = asignaturas = None

        try:
            tareas = Tarea.objects.filter(
                estudiante__user_id=self.request.user.id,
                estado=Tarea.ENVIADA
            )
            cant_tareas = tareas.count()
            list_tareas = tareas[:5]
        except:
            list_tareas = cant_tareas = tareas = None

        try:
            clases = Clase.objects.filter(
                estudiante__user_id=self.request.user.id
            )
            cant_clases = clases.count()
            list_clases = clases[:5]
        except:
            list_clases = cant_clases = clases = None

        context = super(ResolverTareas, self).get_context_data(**kwargs)

        context.update(
            {
                'Title': 'Tarea: ' + assigment.titulo,
                'tipo_usuario': tipo_usuario,
                'on_screen': 'tareas_pendientes',

                'subjects_count': cant_asignaturas,
                'tasks_count': cant_tareas,
                'classes_count': cant_clases,

                'task_content': assigment,
                'task_student': student_assigment,
            }
        )

        return context

    def get(self, request, *args, **kwargs):

        try:
            tarea = Tarea.objects.get(id=self.kwargs.get('assigment_pk'), estudiante__user_id=self.request.user.id)
            solucion = SolucionTarea.objects.get(tarea=tarea)
            if tarea == solucion.tarea:
                return redirect('vista_tareas_resueltas', pk=solucion.pk)
        except:
            return super().get(request, *args, **kwargs)


class DetalleTareas(DetailView):

    model = SolucionTarea
    template_name = 'respuestas_detalles.html'

    def get_context_data(self, **kwargs):

        tipo_usuario = Group.objects.get(user=self.request.user).name

        try:
            asignaturas = Asignatura.objects.filter(curso__estudiante__user_id=self.request.user)
            cant_asignaturas = asignaturas.count()
        except:
            cant_asignaturas = asignaturas = None

        try:
            tareas = Tarea.objects.filter(
                estudiante__user_id=self.request.user.id,
                estado=Tarea.ENVIADA
            )
            cant_tareas = tareas.count()
            list_tareas = tareas[:5]
        except:
            list_tareas = cant_tareas = tareas = None

        try:
            clases = Clase.objects.filter(
                estudiante__user_id=self.request.user.id
            )
            cant_clases = clases.count()
            list_clases = clases[:5]
        except:
            list_clases = cant_clases = clases = None

        context = super(DetalleTareas, self).get_context_data(**kwargs)

        context.update(
            {
                'Title': 'Contenido de la lección',
                'tipo_usuario': tipo_usuario,
                'on_screen': 'contenido_clases',

                'subjects_count': cant_asignaturas,
                'tasks_count': cant_tareas,
                'classes_count': cant_clases,

                'tasks_list': list_tareas,
                'classes_list': list_clases,
            }
        )

        return context


class ListaClases(ListView):

    paginate_by = 5
    model = Clase
    template_name = 'clases.html'
    queryset = Clase.objects.all()

    def get_queryset(self):
        return Clase.objects.filter(curso__estudiante__user_id=self.request.user.id)

    def get_context_data(self, **kwargs):

        tipo_usuario = Group.objects.get(user=self.request.user).name

        try:
            asignaturas = Asignatura.objects.filter(curso__estudiante__user_id=self.request.user)
            cant_asignaturas = asignaturas.count()
        except:
            cant_asignaturas = asignaturas = None

        try:
            tareas = Tarea.objects.filter(
                estudiante__user_id=self.request.user.id,
                estado=Tarea.ENVIADA
            )
            cant_tareas = tareas.count()
            list_tareas = tareas[:5]
        except:
            list_tareas = cant_tareas = tareas = None

        try:
            clases = Clase.objects.filter(
                estudiante__user_id=self.request.user.id
            )
            cant_clases = clases.count()
            list_clases = clases[:5]
        except:
            list_clases = cant_clases = clases = None

        context = super(ListaClases, self).get_context_data(**kwargs)

        context.update(
            {
                'Title': 'Mis lecciones',
                'tipo_usuario': tipo_usuario,
                'on_screen': 'contenido_clases',

                'subjects_count': cant_asignaturas,
                'tasks_count': cant_tareas,
                'classes_count': cant_clases,

                'tasks_list': list_tareas,
                'classes_list': list_clases,
            }
        )

        return context


class DetalleClases(DetailView):

    model = Clase
    template_name = 'clases_detalles.html'

    def get_context_data(self, **kwargs):

        tipo_usuario = Group.objects.get(user=self.request.user).name

        try:
            asignaturas = Asignatura.objects.filter(curso__estudiante__user_id=self.request.user)
            cant_asignaturas = asignaturas.count()
        except:
            cant_asignaturas = asignaturas = None

        try:
            tareas = Tarea.objects.filter(
                estudiante__user_id=self.request.user.id,
                estado=Tarea.ENVIADA
            )
            cant_tareas = tareas.count()
            list_tareas = tareas[:5]
        except:
            list_tareas = cant_tareas = tareas = None

        try:
            clases = Clase.objects.filter(
                estudiante__user_id=self.request.user.id
            )
            cant_clases = clases.count()
            list_clases = clases[:5]
        except:
            list_clases = cant_clases = clases = None

        context = super(DetalleClases, self).get_context_data(**kwargs)

        context.update(
            {
                'Title': 'Contenido de la lección',
                'tipo_usuario': tipo_usuario,
                'on_screen': 'contenido_clases',

                'subjects_count': cant_asignaturas,
                'tasks_count': cant_tareas,
                'classes_count': cant_clases,

                'tasks_list': list_tareas,
                'classes_list': list_clases,
            }
        )

        return context
