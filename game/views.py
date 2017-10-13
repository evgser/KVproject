from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import Http404
from django.contrib import auth
from django.template.context_processors import csrf
from .models import Game, GameInfo, City, Person
from django.contrib.auth.decorators import login_required

@login_required(login_url='/person/login')
def my_game(request):
    args = {}
    args.update(csrf(request))
    # Получение текущего пользователя из User
    args['username'] = request.user
    # Получаем пользователя из Person
    p = Person.objects.get(user=args['username'].id)

    args['my_games'] = GameInfo.objects.filter(game__user_id=p)


    return render(request, 'game/my-game.html', args)

def game(request):
    args = {}
    args.update(csrf(request))
    # Получение текущего пользователя из User
    args['username'] = request.user

    args['all_games'] = GameInfo.objects.all()

    return render(request, 'game/game.html', args)


def create_game(request):
    args = {}
    args.update(csrf(request))
    # Получение текущего пользователя из User
    args['username'] = request.user
    # Получаем список городов для выбора
    args['cities'] = City.objects.all()
    # Получаем пользователя из Person
    p = Person.objects.get(user=args['username'].id)

    if request.POST:
        g = Game(user_id=p)
        g.save()
        g_info = GameInfo(name=request.POST['name_game'],
                          game=g,
                          city=args['cities'].get(id=request.POST['city_choice']))
        g_info.save()
        return redirect('game:my-game')

    return render(request, 'game/create-game.html', args)

def join_game(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['games'] = GameInfo.objects.all()
    return render(request, 'game/join-game.html', args)
