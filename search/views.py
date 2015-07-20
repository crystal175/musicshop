from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Artist, Song
from .forms import SearchForm

from django.core import serializers


def main(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            mess = form.cleaned_data['query']

            #res = serializers.serialize('json', Artist.objects.filter(name__icontains=mess))
            #request.session["new"] = res
            #return redirect('/search/result/')
            return HttpResponse('result > %s' % mess)
    else:
        # GET /search/
        form = SearchForm()
    return render(request, 'search/main.html', {'form': form})


def result(request):
    data = request.session["new"]
    del request.session["new"]
    data2 = list(serializers.deserialize('json', data))



    return HttpResponse('result > %s' % data)
