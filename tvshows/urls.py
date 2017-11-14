from django.conf.urls import url
from . import views

app_name = 'tvshows'
urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^seasons/$', views.seasons, name = 'season'),
    url(r'^seasons/(?P<Tvseries_id>[0-9]+)/$', views.seasons, name='season'),
    ]