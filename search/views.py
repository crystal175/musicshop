from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse

from .models import Artist, Song
from .forms import SearchForm

import json


def main(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            mess = form.cleaned_data['query']
            request.session["new"] = mess
    else:
        # GET /search/
        form = SearchForm()
    return render(request, 'search/main.html', {'form': form})


def ajax_result(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            mess = form.cleaned_data['query']
        else:
            mess = 'Bad request'

        mess_len = len(mess)

        try:
            artist = Artist.objects.filter(name__icontains=mess[0])
        except Artist.DoesNotExist:
            pass

        if mess_len == 1:
            if artist:
                # search all song of artist
                # in template
                pass
            else:
                # search in songs
                song = Song.objects.filter(title__icontains=mess[0])   
        
        if mess_len == 2:
            # artist and song
            try:
                song = Song.objects.filter(title__icontains=mess[1])
            except Song.DoesNotExist:
                pass
            if artist and song:
                # search song of artist
                song = Song.objects.filter(
                    title__icontains=mess[1]).filter(
                        artist__name__icontains=mess[0])
            else:
                # search in songs(only song)
                song = Song.objects.filter(title__icontains=mess[1])

        return render(request, 'search/ajax_result.html', locals())
    '''
    return render(request, 'search/ajax-result.html', {
        'artist': artist,
        'song': song,
        'form_errors': form.errors
        })
    '''

    #1 json
    '''
    return HttpResponse(
        json.dumps(res),
        content_type="application/json")
    '''
    '''
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
    '''

def order(request, pk):
    song = Song.objects.get(id=pk)
    return render(request, 'search/order_song.html', {'song': song})