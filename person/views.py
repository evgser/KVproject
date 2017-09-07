from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import Http404
from django.contrib import auth
from django.template.context_processors import csrf


def cabinet(request):

    try:
        args = {}
        args.update(csrf(request))
        args['username'] = auth.get_user(request).username
        args['text'] = 'Чё кого, сучааара'
        #obj = get_object_or_404(models.Account, pk = login)
        #return render(request, 'landing/cabinet.html', {'obj': obj})
    except args.DoesNotExist:
        raise Http404("Накосячил, мудила")
    return render(request, 'landing/cabinet.html', args)

# Функция для авторизации пользователя
def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = 'Пользователь не найден'
            return render_to_response('landing/login.html', args)
    else:
        return render_to_response('landing/login.html', args)


def logout(request):
    auth.logout(request)
    return redirect("/")

