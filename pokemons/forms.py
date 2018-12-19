from django import forms
from django.contrib.auth.models import User

from .models import Pokemon


class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='Логин', max_length=50)
    first_name = forms.CharField(label='Имя', max_length=50)
    last_name = forms.CharField(label='Фамилия', max_length=50)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)
    email = forms.EmailField(label='Электроннная почта')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'password2', 'email']


# class LoginModelForm(forms.ModelForm):
#     username = forms.CharField(label='Логин', max_length=50)
#     password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ['username', 'password']


class PokemonModelForm(forms.ModelForm):

    # class UploadFileForm(forms.Form):
    #     img = forms.FileField()

    class Meta:
        model = Pokemon
        fields = ['name', 'weight', 'gender', 'talents', 'type', 'photo']


# class UploadFileForm(forms.Form):
#         title = forms.CharField(max_length=50)
#         img = forms.FileField()
