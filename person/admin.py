from django.contrib import admin
from .models import Person

# Админка для Person
class PersonAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name','last_name','phone', 'sub_email', 'city')

admin.site.register(Person, PersonAdmin)


