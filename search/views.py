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
            return redirect('/search/result/')
    else:
        # GET /search/
        form = SearchForm()
    return render(request, 'search/main.html', {'form': form})


def result(request):
    data = request.session["new"]
    #del request.session["new"]

    artist = False
    try:
        artist = Artist.objects.filter(name__icontains=data[0])
    except Artist.DoesNotExist:
        pass

    res = {}
    data_len = len(data)

    if data_len == 2:
        # artist and song
        if artist:
            # search song of artist
            for a in artist:
                res[a] = a.song_set.all().filter(title__icontains=data[1])
        else:
            # search in songs
            song = Song.objects.filter(title__icontains=data[1])
            for s in song:
                res[s.name] = s
    else:
        # artist or song, data_len == 1
        if artist:
            # search all song of artist
            for a in artist:
                res[a] = a.song_set.all()
        else:
            # search in songs
            song = Song.objects.filter(title__icontains=data[0])
            for s in song:
                res[s.name] = s

    return render(request, 'search/res2.html', locals())


def hello(request):
    if request.method == 'POST':
        response_data = request.POST.get('search_text')
        res = {}
        mysong = Song.objects.filter(title__icontains=response_data)
        for m in mysong:
            res[m.title] = m.title

        return render(request, 'search/ajax-result.html', locals())

        #2 plain res 
        #return HttpResponse(res)


        #1 json
        '''
        return HttpResponse(
            json.dumps(res),
            content_type="application/json")
        '''
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
