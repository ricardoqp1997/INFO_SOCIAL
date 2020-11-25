from django import forms
from django.contrib.auth import authenticate

from .models import *


# Form de inicio de sesión para usuarios
class UserLoginForm(forms.Form):
    username = forms.CharField(
        label='Usuario',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Usuario',
                'autofocus': 'autofocus'
            }
        ),
        required=True
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Contraseña',
            }
        ),
        required=True
    )

    def clean(self, *args, **kwargs):

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:

            user = authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError('Por favor verifique los datos de usuario ingresados.')
            if not user.check_password(password):
                raise forms.ValidationError('Por favor verifique la contraseña ingresada.')
            if not user.is_active:
                raise forms.ValidationError('El usuario ingresado no está activo.')

        return super(UserLoginForm, self).clean()


class AssigmentForm(forms.ModelForm):
    pass


class AssigmentResolution(forms.ModelForm):

    estado = forms.CharField(
        widget=forms.HiddenInput(),
        required=False
    )
    estudiante = forms.IntegerField(
        widget=forms.HiddenInput(),
        required=False
    )
    tarea = forms.IntegerField(
        widget=forms.HiddenInput(),
        required=False
    )
    anotaciones = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control'
            }
        ),
        label='Resolución o comentarios',
        help_text='En este apartado irán las respuestas (si así se requieren) o comentarios adicionales respecto'
                  'a la entrega de la tarea. Recuerde que la prioridad de solución de la tarea es por medio de '
                  'archivos adjuntos.',
        max_length=400,
        required=True
    )
    adjuntos = forms.FileField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-control-file'
            }
        ),
        label='Archivo adjunto de tarea',
        help_text='Es requerido subir la solución a la tarea por medio de un archivo adjunto.',
        required=True
    )

    class Meta:
        model = SolucionTarea
        fields = [
            'estudiante',
            'tarea',
            'anotaciones',
            'adjuntos',
        ]
