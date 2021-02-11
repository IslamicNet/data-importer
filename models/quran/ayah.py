from fireo.models import Model
from fireo.fields import IDField, NumberField, MapField

class Ayah(Model):
    id = IDField()
    number = NumberField()
    surah_number = NumberField()
    content = MapField()

    class Meta:
        collection_name = "quran"