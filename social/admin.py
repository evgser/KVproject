from django.contrib import admin
from social.models import Team, MemberTeam
from person.models import Person

# Админка для команд
class MemberTeamInline(admin.TabularInline):
    model = MemberTeam
    extra = 1

class TeamAdmin(admin.ModelAdmin):
    #list_display = ('name', 'members')
    inlines = (MemberTeamInline,)

admin.site.register(Team, TeamAdmin)

