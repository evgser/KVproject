from django.db import models
from game.models import GameInfo
from social.models import Team


class Session(models.Model):
    name = models.CharField(max_length=32, verbose_name='Имя для проведенной игры')
    count_team = models.IntegerField(verbose_name='Количество команд', default=0)
    status = models.IntegerField(verbose_name='Статус игры')
    games = models.ManyToManyField(GameInfo)
    teams = models.ManyToManyField(Team)

    class Meta:
        verbose_name = 'Игровая сессия'
        verbose_name_plural = 'Игровые сессии'

    def __str__(self):
        return self.name