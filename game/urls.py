from django.conf.urls import url
from game import views

app_name = 'game'
urlpatterns = [
    url(r'^$', views.game, name='game'),
    url(r'^my-game/', views.my_game, name='my-game'),
    url(r'^create-game/$', views.create_game, name='create-game'),
    url(r'^join-game/$', views.join_game),
]