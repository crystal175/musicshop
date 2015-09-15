from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^ajax_search/$', views.ajax_search, name='ajax_search'),
    url(r'^(?P<pk>[0-9]+)/$', views.order, name='order'),
    url(r'^thanks/$', views.thanks, name='thanks'),

]
