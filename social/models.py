from django.db import models
from person.models import Person


class Team(models.Model):
    name = models.CharField(max_length=32, verbose_name='Название команды')
    lead = models.ForeignKey(Person, verbose_name='Лидер')

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

    def __str__(self):
        return 'Команда: %s' % self.name

class PersonTeam(models.Model):
    person_id = models.ForeignKey(Person)
    team_id = models.ForeignKey(Team)
    role = models.BooleanField(verbose_name='Роль')
