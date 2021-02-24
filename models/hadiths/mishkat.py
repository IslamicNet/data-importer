from fireo.models import Model
from fireo.fields import IDField, NumberField, MapField, TextField, BooleanField


class Mishkat(Model):
    id = IDField()
    hadith_number = NumberField()
    book_number = NumberField()
    book_name = MapField()
    chapter = MapField()
    text = MapField()
    grade = MapField()
    is_sahih = BooleanField()
    uci = TextField(required=True)

    class Meta:
        collection_name = "mishkat"
