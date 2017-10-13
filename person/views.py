from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import Http404
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from person.models import Person
from landing.models import City

@login_required(login_url='/person/login')
def cabinet(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['user'] = auth.get_user(request)

    Person.objects.get_or_create(user=args['user'])

    args['p'] = Person.objects.get(user=args['user'])

    args['cities'] = City.objects.all()

    if request.POST:

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        if phone == '':
            phone = None
        sub_email = request.POST['sub_email']
        city_choice = request.POST.get('city_choice', None)
        Person.objects.filter(user=args['user']).update(first_name=first_name, last_name=last_name,
                                                      phone=phone, sub_email=sub_email)
        if city_choice:
            Person.objects.filter(user=args['user']).update(city=City.objects.get(city=city_choice))

        return redirect('/person/')
    else:
        return render(request, 'person/cabinet.html', args)

# Функция для авторизации пользователя
def login(request):
    args = {}
    args.update(csrf(request))
    if not request.user.is_authenticated:
        if request.POST:
            args['username'] = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=args['username'], password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                args['login_error'] = 'Пользователь не найден'
                return render_to_response('person/login.html', args)
        else:
            return render_to_response('person/login.html', args)
    else:
        return redirect('/person/')


def logout(request):
    auth.logout(request)
    return redirect("/")

