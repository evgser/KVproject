from django.db import models
from datetime import *
from django.contrib.auth.models import User

'''
class Account(models.Model):
    login = models.CharField(max_length=16, verbose_name='Логин')
    password = models.CharField(max_length=32, verbose_name='Пароль')
    email = models.EmailField(verbose_name='Эл. почта')

    class Meta:
        verbose_name = 'Аккаунт пользователя'
        verbose_name_plural = 'Аккаунты пользователей'

    def __str__(self):
        return self.login
'''

class City(models.Model):
    city = models.CharField(max_length=32, verbose_name='Город')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.city

class Person(models.Model):
    first_name = models.CharField(max_length=32, verbose_name='Имя')
    last_name = models.CharField(max_length=32, verbose_name='Фамилия')
    phone = models.IntegerField(verbose_name='Телефон')
    sub_email = models.EmailField(verbose_name='Доп. эл. почта')

    city = models.ForeignKey(City, verbose_name='Город')
    account_id = models.ForeignKey(User, verbose_name='Логин')

    class Meta:
        verbose_name = 'Персональные данные'
        verbose_name_plural = 'Персональные данные'

class Game(models.Model):

    name = models.CharField(default='name', max_length=16, verbose_name='Название игры')
    #key = models.IntegerField(unique='true', verbose_name='Ключ игры')
    #password = models.CharField(max_length=32, verbose_name='Пароль от игры')

    city = models.ForeignKey(City, verbose_name='Город', default=1)
    account_id = models.ForeignKey(User, verbose_name='Логин')

    class Meta:
        verbose_name = 'Созданная игра'
        verbose_name_plural = 'Созданные игры'


class GameInfo(models.Model):
    name = models.CharField(max_length=16, verbose_name='Название игры')
    info = models.TextField(verbose_name='Описание игры')
    image = models.ImageField(verbose_name='Картинка к игре')

    game_id = models.ForeignKey(Game, verbose_name='ID игры')
    city = models.ForeignKey(City, verbose_name='Город')

    class Meta:
        verbose_name = 'Информация об игре'
        verbose_name_plural = 'Информация об играх'

class Session(models.Model):
    name = models.CharField(max_length=32, verbose_name='Имя для проведенной игры')
    count_team = models.IntegerField(verbose_name='Количество команд')

class Team(models.Model):
    name = models.CharField(max_length=32, verbose_name='Название команды')

# 3 связующие БД, многие ко многим)
class GameSession(models.Model):
    game_id = models.ForeignKey(Game)
    session_id = models.ForeignKey(Session)

class SessionTeam(models.Model):
    session_id = models.IntegerField()
    team_id = models.IntegerField()

class PersonTeam(models.Model):
    person_id = models.ForeignKey(Person)
    team_id = models.ForeignKey(Team)

# Результат, хз так ли надо
class Result(models.Model):
    score = models.IntegerField(verbose_name='Счёт команды')

    team_id = models.ForeignKey(Team)
    session_id = models.ForeignKey(Session)
    game_id = models.ForeignKey(Game)