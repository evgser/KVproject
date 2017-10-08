from django.db import models
from django.contrib.auth.models import User
from landing.models import City

class Person(models.Model): # Добавить валидатор и проверку на авторизацию !!!
    """Модель для хранения информации о пользователях"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, verbose_name='Логин', default=None)
    first_name = models.CharField(max_length=32, verbose_name='Имя', null=True) # ?
    last_name = models.CharField(max_length=32, verbose_name='Фамилия', null=True) # ?
    #photo = models.ImageField()
    phone = models.IntegerField(verbose_name='Телефон', null=True, blank=True)
    sub_email = models.EmailField(verbose_name='Доп. эл. почта', null=True)

    city = models.ForeignKey(City, verbose_name='Город', null=True, default=None, blank=True)

    class Meta:
        verbose_name = 'Персональные данные'
        verbose_name_plural = 'Персональные данные'

    def __str__(self):
        return 'Пользователь: %s, %s %s' % (self.user_id, self.first_name, self.last_name)