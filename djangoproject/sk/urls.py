from django.conf.urls import url
from django.urls import path
from . import views

app_name = "sk"

urlpatterns = [
    # sk/
    url(r'^$', views.IndexView.as_view(),name='sk-index'),

    # # sk/1
    # path('<int:project_id>/',views.DetailsView.as_view(),name='sk-detail'),

    # /sk/71/
    url('^(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name='sk-detail'),
]