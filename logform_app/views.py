
from django.contrib import auth
from django.shortcuts import render, HttpResponseRedirect
from django.http import Http404
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


def login(request):
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'auth.html', {'username ': username, 'errors': True})
    raise Http404

def logout(request):
    pass

def registration(request):
    if request.method == 'POST':
        try:
            errors = {}
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('confirm_password')
            print(request.POST)
            if password != password2:
                errors['password'] = 'Введёные пароли не совпадают!'
            user = User( username=username, email=email)
            user.set_password(password)
            user.validate_unique()
            user.save()
        except ValidationError as er:
            errors = {}
            errors.update(er.message_dict)
            if errors:
                return render(request, 'auth.html', {'reg_errors': errors})
            return HttpResponseRedirect("/")
        return render(request, 'auth.html')
