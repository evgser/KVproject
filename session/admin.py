from django.contrib import admin
from .models import Session

class SessionAdmin(admin.ModelAdmin):
   list_display = ('name', 'status', 'count_team')

admin.site.register(Session, SessionAdmin)