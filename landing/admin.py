from django.contrib import admin
from . import models

# Админка для City
admin.site.register(models.City)

# Админка для Person
class PersonAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name','last_name','phone', 'sub_email', 'city')

admin.site.register(models.Person, PersonAdmin)

# Админка для Game
class GameAdmin(admin.ModelAdmin):
   list_display = ('name', 'user_id')

admin.site.register(models.Game, GameAdmin)

# Админка для GameInfo
class GameInfoAdmin(admin.ModelAdmin):
    list_display = ('game', 'info', 'city')

admin.site.register(models.GameInfo, GameInfoAdmin)
