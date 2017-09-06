from django.db import models
from datetime import *
from django.contrib.auth.models import User

class City(models.Model):
    city = models.CharField(max_length=32, verbose_name='Город')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.city

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, verbose_name='Логин')
    first_name = models.CharField(max_length=32, verbose_name='Имя') # ?
    last_name = models.CharField(max_length=32, verbose_name='Фамилия') # ?
    phone = models.IntegerField(verbose_name='Телефон')
    sub_email = models.EmailField(verbose_name='Доп. эл. почта')

    city = models.ForeignKey(City, verbose_name='Город')

    class Meta:
        verbose_name = 'Персональные данные'
        verbose_name_plural = 'Персональные данные'

class Game(models.Model):
    name = models.CharField(default='name', max_length=16, verbose_name='Название игры')
    #key = models.IntegerField(unique='true', verbose_name='Ключ игры')
    #password = models.CharField(max_length=32, verbose_name='Пароль от игры')

    user_id = models.ForeignKey(User, verbose_name='Логин')

    class Meta:
        verbose_name = 'Созданная игра'
        verbose_name_plural = 'Созданные игры'

    def __str__(self):
        return self.name


class GameInfo(models.Model):
    game = models.OneToOneField(Game, on_delete=models.CASCADE, primary_key=True, verbose_name='ID игры')
    info = models.TextField(verbose_name='Описание игры')
    image = models.ImageField(verbose_name='Картинка к игре')

    city = models.ForeignKey(City, verbose_name='Город')

    class Meta:
        verbose_name = 'Информация об игре'
        verbose_name_plural = 'Информация об играх'


class Session(models.Model):
    name = models.CharField(max_length=32, verbose_name='Имя для проведенной игры')
    count_team = models.IntegerField(verbose_name='Количество команд')
    status = models.IntegerField(verbose_name='Статус игры')

    class Meta:
        verbose_name = 'Игровая сессия'
        verbose_name_plural = 'Игровые сессии'

class Team(models.Model):
    name = models.CharField(max_length=32, verbose_name='Название команды')
    lead = models.ForeignKey(Person, verbose_name='Лидер')

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

# 3 связующие БД, многие ко многим)
class GameSession(models.Model):
    game_id = models.ForeignKey(Game)
    session_id = models.ForeignKey(Session)

    class Meta:
        verbose_name = 'Сессия у игры'
        verbose_name_plural = 'Сессии у игр'

class SessionTeam(models.Model):
    session_id = models.IntegerField()
    team_id = models.IntegerField()
    results = models.IntegerField(verbose_name='Результаты')

    class Meta:
        verbose_name = 'Сессия у команды'
        verbose_name_plural = 'Сессии у команд'

class PersonTeam(models.Model):
    person_id = models.ForeignKey(Person)
    team_id = models.ForeignKey(Team)
    role = models.BooleanField(verbose_name='Роль')