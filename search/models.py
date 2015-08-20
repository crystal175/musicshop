from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=30, unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        """ Ordedering output by name. """
        ordering = ["name"]


class Song(models.Model):
    artist = models.ForeignKey(Artist, related_name='songs')
    title = models.CharField(max_length=50, unique=True, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        """ Ordedering output by title. """
        ordering = ["title"]

class Order(models.Model):
    song = models.ForeignKey(Song, related_name='orders')
    address = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    comment = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0} - {1} | {2}'.format(
            self.song.artist,
            self.song,
            self.date.time())
