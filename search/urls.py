from django.conf.urls import url

from .views import SongCreate, SongList, SuccessView, main, ajax_search, order

urlpatterns = [
    url(r'^$', main, name='main'),
    url(r'^ajax-search/$', ajax_search, name='ajax_search'),
    url(r'^create-song/$', SongCreate.as_view(), name='create_song'),
    url(r'^song-list/$', SongList.as_view(), name='song_list'),
    url(r'^thanks/$', SuccessView.as_view(), name='thanks'),
    url(r'^(?P<pk>[0-9]+)/$', order, name='order'),

]
