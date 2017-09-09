from django.db import models
from person.models import Person


class Team(models.Model):
    """Модель для хранения команд"""
    name = models.CharField(max_length=32, verbose_name='Название команды')
    lead = models.ForeignKey(Person, verbose_name='Лидер')

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

    def __str__(self):
        return 'Команда: %s' % self.name

class Role(models.Model):
    """Модель для хранения ролей игроков в командах"""
    role = models.BooleanField(verbose_name='Роль')
    person_id = models.ForeignKey(Person)
    team_id = models.ForeignKey(Team)

    class Meta:
        verbose_name = 'Роль игрока в команде'
        verbose_name_plural = 'Роли игрков в командах'

    def __str__(self):
        return self.role # ?
