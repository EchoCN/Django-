from haystack import indexes
from .models import Player


class GoodsIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True,use_template=True)

    def get_model(self):
        return Player

    def index_queryset(self, using=None):
        return self.get_model().objects.all()