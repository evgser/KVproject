from django.contrib import admin
from . import models

#class PersonAdmin(admin.ModelAdmin):
#    list_display = ('user_id', 'first_name','last_name','phone', 'sub_email', 'city')

#class GameAdmin(admin.ModelAdmin):
#    list_display = ('name', 'user_id')

admin.site.register(models.Game)

admin.site.register(models.Person)

admin.site.register(models.City)
