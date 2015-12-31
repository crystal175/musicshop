from django.conf.urls import url

from .views import SongCreate, SuccessView, main, ajax_search, order

urlpatterns = [
    url(r'^$', main, name='main'),
    url(r'^ajax_search/$', ajax_search, name='ajax_search'),
    url(r'^(?P<pk>[0-9]+)/$', order, name='order'),
    url(r'^create-song/$', SongCreate.as_view(), name='create'),
    url(r'^thanks/$', SuccessView.as_view(), name='thanks'),

]
