from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.models import User


def registration(request): # Добавить валидатор на проверку формы и проверку на активированность пользователя
    """Регистрация новых пользователей"""
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            if user is not None:
                auth.login(request, user)
                return redirect('/')
        else:
            args['password_error'] = 'Пароли не совпадают'
    return render(request, 'landing/registration.html', args)