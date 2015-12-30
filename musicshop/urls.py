from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', include('search.urls', namespace="search")),
    url(r'^hsearch/', include('haystack.urls')),
]
