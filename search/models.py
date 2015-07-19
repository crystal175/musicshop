from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=30, unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        """ Ordedering output by name. """
        ordering = ["name"]


class Song(models.Model):
    name = models.ForeignKey(Artist)
    title = models.CharField(max_length=50, unique=True, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        """ Ordedering output by title. """
        ordering = ["title"]
