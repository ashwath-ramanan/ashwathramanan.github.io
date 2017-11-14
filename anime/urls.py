from django.conf.urls import url
from . import views

app_name = 'anime'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^arcs/$', views.arc, name = 'arcs'),
    url(r'^arcs/(?P<animeseries_id>[0-9]+)/$', views.arc, name='arc'),

    ]