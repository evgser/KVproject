from django.conf.urls import url
from registration import views

app_name = 'registration'
urlpatterns = [
    url(r'^registration/$', views.registration),
]