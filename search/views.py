from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Artist, Song
from .forms import SearchForm


def main(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            mess = request.POST['query']
            request.session["new"] = mess
            return redirect('/search/result/')
    else:
        # GET /search/
        form = SearchForm()
    return render(request, 'search/main.html', {'form': form})


def result(request):
    sn = request.session["new"]
    del request.session["new"]
    return HttpResponse('result > %s' % sn)
