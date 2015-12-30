from django.conf.urls import url

from .views import SongCreate, main, ajax_search, order, thanks

urlpatterns = [
    url(r'^$', main, name='main'),
    url(r'^ajax_search/$', ajax_search, name='ajax_search'),
    url(r'^(?P<pk>[0-9]+)/$', order, name='order'),
    url(r'^thanks/$', thanks, name='thanks'),
    url(r'^create-song/$', SongCreate.as_view(), name='create'),

]
