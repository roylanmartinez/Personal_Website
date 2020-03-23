from django import forms
from .models import Contactt


class Contactf(forms.ModelForm):

    class Meta():
        model = Contactt
        fields = ['email', 'name', 'text']
        labels = {
            'email': 'Email', 'Name': 'name', 'Text': 'message'
        }
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'style': 'background-color: black',
                'placeholder': 'Your Email',
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'background-color: black',
                'placeholder': 'Your Name'}),
            'text': forms.Textarea(attrs={
                'rows': 3,
                'style': 'background-color: black',
                'class': 'form-control',
                'placeholder': 'Hello Roylan,'})
        }


class Contactfes(forms.ModelForm):

    class Meta():
        model = Contactt
        fields = ['email', 'name', 'text']
        labels = {
            'email': 'Correo', 'name': 'Nombre', 'text': 'Mensaje'
        }
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'style': 'background-color: black',
                'placeholder': 'Tu Correo',
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'background-color: black',
                'placeholder': 'Tu Nombre'}),
            'text': forms.Textarea(attrs={
                'rows': 3,
                'style': 'background-color: black',
                'class': 'form-control',
                'placeholder': 'Hola Roylan,'})
        }
