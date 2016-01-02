from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.views.generic import CreateView, TemplateView, ListView
from musicshop.settings import EMAIL_HOST_USER

from .models import Artist, Song, Order
from .forms import SearchForm, OrderForm


class SongCreate(CreateView):
    model = Song
    template_name = 'search/create_song.html'
    fields = ['artist', 'title']

    def get_success_url(self):
        return reverse('search:thanks',)


class SongList(ListView):
    model = Song
    context_object_name = 'song_list'


class SuccessView(TemplateView):
    template_name = "search/thanks.html"


def main(request):
    """ Main page view. """
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            mess = form.cleaned_data['query']
            request.session["new"] = mess
    else:
        # GET /search/
        form = SearchForm()
    return render(request, 'search/main.html', {'form': form})


def ajax_search(request):
    """ Ajax search view that takes 1 or 2 words. """
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            mess = form.cleaned_data['query']
        else:
            mess = 'Bad request'

        mess_len = len(mess)
        artist = False
        song = False
        try:
            artist = Artist.objects.filter(name__icontains=mess[0])
        except Artist.DoesNotExist:
            pass

        if mess_len == 1:
            if artist:
                # search all song of artist, iterate in template
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
        return render(request, 'search/ajax_search.html', {
            'artist': artist,
            'song': song,
            'form_errors': form.errors
        })


def order(request, pk):
    """ View that accept and save music order to database. """
    song = Song.objects.get(id=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=song)
        if form.is_valid():
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            comment = form.cleaned_data['comment']
            message = 'Your order is {0} - {1}'.format(song.artist.name, song)
            sender = EMAIL_HOST_USER
            Order.objects.create(song=song, email=email, address=address,
                                 name=name, surname=surname, comment=comment)
            send_mail('Musicshop', message, sender, [email])
            return redirect(reverse('search:thanks'))
    else:
        form = OrderForm(initial={'song': song.id})
    return render(request, 'search/order_song.html',
                  {'song': song, 'form': form})
