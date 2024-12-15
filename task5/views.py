from django.http import HttpResponse
from django.shortcuts import render


users = ['John', 'Jack', 'User', 'Maike']
info = []


def sign_up_by_html(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        repeat_password = request.POST['repeat_password']
        age = request.POST['age']
        return HttpResponse("")

    return render(request, 'registration_page.html')
