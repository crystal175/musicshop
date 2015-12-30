from django.conf.urls import url

from . import views
from .views import SongCreate

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^ajax_search/$', views.ajax_search, name='ajax_search'),
    url(r'^(?P<pk>[0-9]+)/$', views.order, name='order'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^new-song/$', SongCreate.as_view(), name='create'),

]
