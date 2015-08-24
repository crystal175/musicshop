from django.contrib import admin

from .models import Artist, Song, Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ['song', 'email', 'date']


admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Order, OrderAdmin)
