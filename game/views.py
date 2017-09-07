from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import Http404
from django.contrib import auth
from django.template.context_processors import csrf
from .models import Game, GameInfo, City

def create_game(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['cities'] = City.objects.all()
    if request.POST:
        game = Game(name=request.POST['name_game'],
                           account_id=auth.get_user(request),
                           city=args['cities'].get(id=request.POST['city_choice']))
        game.save()
        return redirect('/')
    return render(request, 'landing/create-game.html', args)

def join_game(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['games'] = GameInfo.objects.all()
    return render(request, 'landing/join-game.html', args)
