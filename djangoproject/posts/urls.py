from django.conf.urls import url

from . import views

app_name = "posts-app"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^details/(?P<id>\d+)/$', views.details, name='details'),
]


