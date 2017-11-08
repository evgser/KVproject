from django.db import models
from django.contrib.auth.models import User
from landing.models import City
from elasticsearch_dsl import DocType, Integer, Text

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


#------------------
# ElasticSearch

class PersonIndex(DocType):
    pk = Integer()
    user = Text()
    first_name = Text()
    last_name = Text()

    class Meta:
        index = 'person'

from rest_framework_elasticsearch.es_serializer import ElasticModelSerializer
#from .models import Person
#from .search_indexes import PersonIndex

class ElasticBlogSerializer(ElasticModelSerializer):
    class Meta:
        model = Person
        es_model = PersonIndex
        fields = ('pk', 'user', 'first_name', 'last_name')

from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
#from .serializers import Person, ElasticPersonSerializer

@receiver(pre_save, sender=Person, dispatch_uid="update_record")
def update_es_record(sender, instance, **kwargs):
    obj = ElasticBlogSerializer(instance)
    obj.save()

@receiver(post_delete, sender=Person, dispatch_uid="delete_record")
def delete_es_record(sender, instance, *args, **kwargs):
    obj = ElasticBlogSerializer(instance)
    obj.delete(ignore=404)