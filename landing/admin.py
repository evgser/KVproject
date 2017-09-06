from django.contrib import admin
from . import models

class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','phone', 'sub_email', 'city', 'account_id')

class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'account_id')

admin.site.register(models.Game, GameAdmin)

admin.site.register(models.Person, PersonAdmin)

admin.site.register(models.City)