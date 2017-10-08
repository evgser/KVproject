from django.conf.urls import url
from social import views

app_name = 'social'
urlpatterns = [
    url(r'^team/$', views.team),
    url(r'^team/(?P<team>[0-9]+)/$', views.team_details, name='team-details'),
    url(r'^create-team/$', views.create_team),
    url(r'^join-team/team=(?P<team>[0-9]+)&user=(?P<user>[0-9]+)$', views.join_team),
    url(r'^invite-team/team=(?P<team>[0-9]+)&user=(?P<user>[0-9]+)$', views.invite_team),
    url(r'^leave-team/team=(?P<team>[0-9]+)&user=(?P<user>[0-9]+)/$', views.leave_team, name='leave-team'),
    url(r'^change-lead/team=(?P<team>[0-9]+)&user=(?P<user>[0-9]+)/$', views.change_lead, name='change-lead'),
]