from django.shortcuts import render, get_object_or_404, redirect, render_to_response

from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from person.models import Person
from social.models import Team, MemberTeam
from django.db.models import Count

@login_required(login_url='/person/login')
def team(request):
    args = {}
    args.update(csrf(request))
    # Получение текущего пользователя из User
    args['username'] = request.user

    # Получаем команды пользователя и количество участников в каждой команде
    # Получаем пользователя
    person = Person.objects.get(user=args['username'])
    # Получаем список всех команд пользователя и количество участников в каждой команде
    args['teams'] = person.team_set.all().annotate(count_person=Count('members'))
    #args['count_members'] =
    args['teams2'] = Team.objects.filter(members=person).annotate(count_person=Count('members'))
    print(args['teams2'][0].count_person)
    print(type(args['teams']))
    print(args['teams'][0].count_person)
    #print(args['teams'][0].members.all().count())

    return render(request, 'social/team.html', args)

@login_required(login_url='/person/login')
def team_details(request, team):
    args = {}
    args.update(csrf(request))
    # Получение текущего пользователя из User
    args['username'] = request.user

    # Получаем команду пользователя
    args['team'] = Team.objects.get(id=team)
    # Получаем всех пользователей команды
    args['members'] = MemberTeam.objects.filter(team_id=args['team'])

    #args['members'] = args['team'].members.all()
    #print(args['team'].members.all().count())

    return render(request, 'social/team-detail.html', args)

@login_required(login_url='/person/login')
def create_team(request):
    args = {}
    args.update(csrf(request))
    # Получение текущего пользователя из User
    args['username'] = request.user

    if request.POST:
        # Получаем пользователя
        person = Person.objects.get(user=args['username'])
        # Получаем название команды, которую хочет создать пользователь
        team_name = request.POST['team_name']

        # Проверям существуют ли уже команда с таким именем
        if Team.objects.filter(name=team_name):
            # Выводим пользователю сообщение об ошибке
            args['team_error'] = 'Команда с таким именем уже существует'
            return render_to_response('social/create-team.html', args) # хуйня, оптимизировать
        else:
            # Если не существует, записываем её в базу данных и задаём её лидера
            t = Team.objects.create(name=team_name, lead=person)
            t.save()
            # Заносим пользователя в команду
            mt = MemberTeam.objects.create(team=t, person=person)
            mt.save()
        return redirect('/social/team/')
    else:
        return render(request, 'social/create-team.html', args)

@login_required(login_url='/person/login')
def join_team(request, team, user):
    pass

@login_required(login_url='/person/login')
def invite_team(request, team):
    args = {}
    args.update(csrf(request))
    # Получение текущего пользователя из User
    args['username'] = request.user

    # Если пользователь лидер команды
    if args['username'] == Team.objects.get(id=team).lead.user:
        # Получаем пользователя
        invite_user = request.POST['invite_user']
        # Отправляем уведомление пользователю о приглашении

    else:
        args['lead_error'] = 'GYP'

    return redirect('social:team-details', team=team)

@login_required(login_url='/person/login')
def leave_team(request, team, user):
    args = {}
    args.update(csrf(request))
    # Получение текущего пользователя из User
    args['username'] = request.user

    # Если пользователь хочет покинуть команду
    if request.user.id == int(user):
        # Если пользователь остался один в команде
        if Team.objects.get(id=team).members.all().count() == 1:
            # Удаляем пользователя из команды
            MemberTeam.objects.get(
                person_id=Person.objects.get(user=args['username']),
                team_id=Team.objects.get(id=team)
            ).delete()
            # Удаляем команду
            Team.objects.get(
                name=Team.objects.get(id=team).name  # Оптимизировать
            ).delete()
        # Если пользователь лидер команды
        elif args['username'] == Team.objects.get(id=team).lead.user:
            # Перенаправляем на смену лидера
            # request.session['lead_error'] = 'Для того, чтобы покинуть команду, необходимо сменить лидера' шляпа полная
            # Получаем команду пользователя
            args['team'] = Team.objects.get(id=team)
            # Получаем всех пользователей команды
            args['members'] = MemberTeam.objects.filter(team_id=args['team'])
            return render(request, 'social/team-detail.html', args) # хуйня, переделать
            #return redirect('social:team-details', team=team)
        # Если пользователь не последний игрок и не лидер
        else:
            # Удаляем пользователя из команды
            MemberTeam.objects.get(
                person_id=Person.objects.get(user=args['username']),
                team_id=Team.objects.get(id=team)
            ).delete()
    # Если лидер удаляет члена команды
    else:
        if args['username'] == Team.objects.get(id=team).lead.user:
            MemberTeam.objects.get(
                person_id=Person.objects.get(user_id=user),
                team_id=Team.objects.get(id=team)
            ).delete()
        return redirect('social:team-details', team=team)

    return redirect('/social/team/')

def change_lead(request, team, user):
    args = {}
    args.update(csrf(request))
    # Получение текущего пользователя из User
    args['username'] = request.user

    # Получаем команду
    t = Team.objects.get(id=team)
    # Если пользователь является лидером
    if args['username'] == t.lead.user:
        # Меняем лидера на выбранного пользователя
        t.lead = Person.objects.get(user_id=user)
        t.save()
    else:
        args['lead_error'] = 'Ты не лидер, иди на хуй'

    return redirect('social:team-details', team=team)



