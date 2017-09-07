from django.conf.urls import url
from game import views

app_name = 'game'
urlpatterns = [
    url(r'^create-game/$', views.create_game),
    url(r'^join-game/$', views.join_game),
]