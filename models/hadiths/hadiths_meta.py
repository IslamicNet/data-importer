from fireo.models import Model
from fireo.fields import IDField, ListField


class HadithsMeta(Model):
    id = IDField()
    books = ListField()

    class Meta:
        collection_name = "hadiths_meta"
