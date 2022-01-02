import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["islamic_content_v1"]
mycol = mydb["hadith_books"]


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
hadith_meta = {
    "_id": "bukhari",
    "books": get_hadith_books(bukhari)
}
mycol.insert_one(hadith_meta)
print("Hadith bukhari meta complete")

muslim_file = open('./data/hadiths/muslim.json', "r", encoding="utf8")
muslim = json.load(muslim_file)
hadith_meta = {
    "_id": "muslim",
    "books": get_hadith_books(muslim)
}
mycol.insert_one(hadith_meta)
print("Hadith muslim meta complete")

tirmidhi_file = open('./data/hadiths/tirmidhi.json', "r", encoding="utf8")
tirmidhi = json.load(tirmidhi_file)
hadith_meta = {
    "_id": "tirmidhi",
    "books": get_hadith_books(tirmidhi)
}
mycol.insert_one(hadith_meta)
print("Hadith tirmidhi meta complete")

abu_dawud_file = open('./data/hadiths/abu_dawud.json', "r", encoding="utf8")
abu_dawud = json.load(abu_dawud_file)
hadith_meta = {
    "_id": "abu_dawud",
    "books": get_hadith_books(abu_dawud)
}
mycol.insert_one(hadith_meta)
print("Hadith abu_dawud meta complete")

nasai_file = open('./data/hadiths/nasai.json', "r", encoding="utf8")
nasai = json.load(nasai_file)
hadith_meta = {
    "_id": "nasai",
    "books": get_hadith_books(nasai)
}
mycol.insert_one(hadith_meta)
print("Hadith nasai meta complete")

ibne_maja_file = open('./data/hadiths/ibne_maja.json', "r", encoding="utf8")
ibne_maja = json.load(ibne_maja_file)
hadith_meta = {
    "_id": "ibne_maja",
    "books": get_hadith_books(ibne_maja)
}
mycol.insert_one(hadith_meta)
print("Hadith ibne_maja meta complete")
