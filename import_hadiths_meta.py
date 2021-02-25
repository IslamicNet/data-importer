import fireo
import json
from models.hadiths.hadiths_meta import HadithsMeta


def get_hadith_books(hadith_collection):
    books_added = []
    books = []
    for hadith in hadith_collection:
        book = {
            "number": int(hadith['Kitab_ID']),
            "urdu": hadith['Kitab'],
            "english": hadith['Kitab_Eng']
        }

        if hadith['Kitab_ID'] not in books_added:
            books_added.append(hadith['Kitab_ID'])
            books.append(book)

    return books


bukhari_file = open('./data/hadiths/bukhari.json', "r", encoding="utf8")
bukhari = json.load(bukhari_file)
hadiths_meta = HadithsMeta()
hadiths_meta.id = "bukhari"
hadiths_meta.books = get_hadith_books(bukhari)
hadiths_meta.save()
print("Hadith bukhari meta complete")

muslim_file = open('./data/hadiths/muslim.json', "r", encoding="utf8")
muslim = json.load(muslim_file)
hadiths_meta = HadithsMeta()
hadiths_meta.id = "muslim"
hadiths_meta.books = get_hadith_books(muslim)
hadiths_meta.save()
print("Hadith muslim meta complete")

tirmidhi_file = open('./data/hadiths/tirmidhi.json', "r", encoding="utf8")
tirmidhi = json.load(tirmidhi_file)
hadiths_meta = HadithsMeta()
hadiths_meta.id = "tirmidhi"
hadiths_meta.books = get_hadith_books(tirmidhi)
hadiths_meta.save()
print("Hadith tirmidhi meta complete")

abu_dawud_file = open('./data/hadiths/abu_dawud.json', "r", encoding="utf8")
abu_dawud = json.load(abu_dawud_file)
hadiths_meta = HadithsMeta()
hadiths_meta.id = "abu_dawud"
hadiths_meta.books = get_hadith_books(abu_dawud)
hadiths_meta.save()
print("Hadith abu_dawud meta complete")

nasai_file = open('./data/hadiths/nasai.json', "r", encoding="utf8")
nasai = json.load(nasai_file)
hadiths_meta = HadithsMeta()
hadiths_meta.id = "nasai"
hadiths_meta.books = get_hadith_books(nasai)
hadiths_meta.save()
print("Hadith nasai meta complete")

ibne_maja_file = open('./data/hadiths/ibne_maja.json', "r", encoding="utf8")
ibne_maja = json.load(ibne_maja_file)
hadiths_meta = HadithsMeta()
hadiths_meta.id = "ibne_maja"
hadiths_meta.books = get_hadith_books(ibne_maja)
hadiths_meta.save()
print("Hadith ibne_maja meta complete")
