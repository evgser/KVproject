from django.contrib import admin
from .models import Game, GameInfo

# Админка для Game
class GameAdmin(admin.ModelAdmin):
   list_display = ('password', 'user_id')

admin.site.register(Game, GameAdmin)

# Админка для GameInfo
class GameInfoAdmin(admin.ModelAdmin):
    list_display = ('game', 'name', 'info', 'city')

admin.site.register(GameInfo, GameInfoAdmin)