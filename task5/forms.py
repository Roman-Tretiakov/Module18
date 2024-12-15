from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(label='Введите логин', max_length=30, required=True)
    password = forms.CharField(label='Введите пароль', min_length=8, required=True)
    repeat_password = forms.CharField(label='Повторите пароль', min_length=8, required=True)
    age = forms.IntegerField(label='Введите свой возраст', max_value=130, required=True)