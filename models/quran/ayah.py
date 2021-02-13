from fireo.models import Model
from fireo.fields import IDField, NumberField, MapField, TextField

class Ayah(Model):
    id = IDField()
    number = NumberField()
    surah_number = NumberField()
    content = MapField()
    uci = TextField(required=True)

    class Meta:
        collection_name = "quran"