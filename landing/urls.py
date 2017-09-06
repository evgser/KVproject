from django.conf.urls import url
from landing import views

app_name = 'landing'
urlpatterns = [
    url(r'^$', views.main),
    url(r'^cabinet/$', views.cabinet),
    url(r'^registration/$', views.registration),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^create-game/$', views.create_game),
    url(r'^join-game/$', views.join_game),
]