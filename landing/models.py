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
