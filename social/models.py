from django.db import models
from person.models import Person


class Team(models.Model):
    """Модель для хранения команд"""
    name = models.CharField(max_length=16, verbose_name='Название команды') # Добавить UNIQ
    lead = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='team_lead',
        verbose_name='Лидер',
        null=True,
    )

    members = models.ManyToManyField(
        Person,
        through='MemberTeam',
        through_fields=('team', 'person'),
    )

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

    def __str__(self):
        return self.name


    #def is_lead(self):
        """Возвращает все команды пользователя и количество участников в команде"""



        #return teams

class MemberTeam(models.Model):
    """Модель для хранения ролей игроков в командах"""
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    role = models.CharField(max_length=16, verbose_name='Роль', null=True, default=None)

    class Meta:
        verbose_name = 'Связь между игроком и командой'
        verbose_name_plural = 'Связь между игроками и командой'

    def __str__(self):
       return '%s - %s' % (self.team, self.person)
