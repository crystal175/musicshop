from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^ajax_result/$', views.ajax_result, name='ajax_result'),
]
