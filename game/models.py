from django.db import models
from person.models import Person
from landing.models import City

class Game(models.Model):
    """Модель для создания игры"""
    password = models.CharField(max_length=32, verbose_name='Пароль от игры')

    user_id = models.ForeignKey(Person, verbose_name='Логин', default=None)

    class Meta:
        verbose_name = 'Созданная игра'
        verbose_name_plural = 'Созданные игры'

    def __str__(self):
        return 'Игра пользователя %s' % self.user_id

class GameInfo(models.Model):
    """Модель для хранения основной информации об игре"""
    game = models.OneToOneField(Game, on_delete=models.CASCADE, primary_key=True, verbose_name='ID игры', default=None)
    name = models.CharField(default='name', max_length=16, verbose_name='Название игры')
    info = models.TextField(verbose_name='Описание игры')
    #image = models.ImageField(verbose_name='Картинка к игре')

    city = models.ForeignKey(City, verbose_name='Город')

    class Meta:
        verbose_name = 'Информация об игре'
        verbose_name_plural = 'Информация об играх'

    def __str__(self):
        return 'Информация по игре %s' % self.game