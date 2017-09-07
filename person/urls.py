from django.conf.urls import url
from person import views

app_name = 'person'
urlpatterns = [
    url(r'^cabinet/$', views.cabinet),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
]