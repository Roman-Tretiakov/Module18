from django.http import HttpResponse
from django.shortcuts import render
from django.template.defaultfilters import title

from task5.forms import UserRegister

users = ['John', 'Jack', 'User', 'Maike']


def sign_up_by_html(request):
    info = {}
    if request.method == "POST":
        info['username'] = username = request.POST['username']
        info['password'] = password = request.POST['password']
        info['repeat_password'] = repeat_password = request.POST['repeat_password']
        info['age'] = age = request.POST['age']

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают!'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18!'
        elif title(username) in users:
            info['error'] = 'Пользователь уже существует!'
        else:
            users.append(title(username))
            info['success_message'] = f'Приветствуем,  {username}!'

        return render(request, 'fifth_task/registration_page.html', context=info)

    return render(request, 'fifth_task/registration_page.html')

def sign_up_by_django(request):
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            info['username'] = username = form.cleaned_data['username']
            info['password'] = password = form.cleaned_data['password']
            info['repeat_password'] = repeat_password = form.cleaned_data['repeat_password']
            info['age'] = age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают!'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18!'
            elif title(username) in users:
                info['error'] = 'Пользователь уже существует!'
            else:
                users.append(title(username))
                info['success_message'] = f'Приветствуем,  {username}!'

            return render(request, 'fifth_task/registration_page.html', context=info)
    else:
        form = UserRegister(request.POST)
        return render(request, 'fifth_task/registration_page.html', {'form': form})


