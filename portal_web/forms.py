from django import forms
from django.contrib.auth import authenticate


# Form de inicio de sesión para usuarios
class UserLoginForm(forms.Form):

    username = forms.CharField(
        label='Usuario',
        widget=forms.TextInput(
            attrs={
                'type': 'email',
                'class': 'form-control',
                'placeholder': 'Usuario',
                'required': 'required',
                'autofocus': 'autofocus'
            }
        )
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
                'class': 'form-control',
                'placeholder': 'Contraseña',
                'required': 'required',
            }
        )
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
