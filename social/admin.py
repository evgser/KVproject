from django.contrib import admin
from .models import Team, Role

# Админка для команд
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'lead')

admin.site.register(Team)

admin.site.register(Role)