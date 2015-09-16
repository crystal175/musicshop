from haystack import indexes
from .models import Song


class SongIndex(indexes.SearchIndex, indexes.Indexable):
    title = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Song
