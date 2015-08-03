from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse

from .models import Artist, Song
from .forms import SearchForm


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
    del request.session["new"]
    data_len = len(data)


    if data_len == 2:
        # artist and song
        artist = False
        try:
            artist = Artist.objects.filter(name__contains=data[0])
        except Artist.DoesNotExist:
            pass

        if artist:
            # if artist and artist.count > 1:
            # search song of artist
            res = {}
            for a in artist:
                res[a] = a.song_set.all().filter(title__contains=data[1])
        else:
            # search in songs
            song = Song.objects.filter(title__contains=data[1])
            res = {}
            for s in song:
                res[s.name] = s


    else:
        # data_len == 1
        artist = False
        try:
            artist = Artist.objects.filter(name__contains=data[0])
        except Artist.DoesNotExist:
            pass

        if artist:
            # if artist and artist.count > 1:
            # search song of artist
            res = {}
            for a in artist:
                res[a] = a.song_set.all()
        else:
            # search in songs
            song = Song.objects.filter(title__contains=data[0])
            res = {}
            for s in song:
                res[s.name] = s



    return render(request, 'search/result.html', locals())

