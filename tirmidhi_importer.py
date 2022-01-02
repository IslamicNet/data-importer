######### UCI ###########
# start number: 358661
# end number: 362617
# Book No: 3
#########################
import pymongo
import json
from uci import UCI

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["islamic_content_v1"]
mycol = mydb["tirmidhi"]

tirmidhi_file = open('./data/hadiths/tirmidhi.json', "r", encoding="utf8")
tirmidhi = json.load(tirmidhi_file)

hadith_batch = []
count = 0
overall_count = 0
uci = UCI(358661)

for hadith in tirmidhi:
    docUCI = uci.next
    ibnemaja = {
        "_id": docUCI,
        "hadithNumber": int(hadith['hadees_number']),
        "bookNumber": int(hadith['Kitab_ID']),
        "bookName": {
            "urdu": hadith['Kitab'],
            "english": hadith['Kitab_Eng']
        },
        "chapter": {
            "urdu": hadith['Baab'],
            "english": hadith['Baab_Eng']
        },
        "arabic": hadith['Arabic'],
        "trnaslations":  {
            "urdu": hadith['Ravi'] + hadith['Urdu'],
            "english": hadith['English']
        },
        "isSahih":  bool(hadith['Sahih_Zaeef']),
        "uci": docUCI
    }

    hadith_batch.append(ibnemaja)

    count += 1
    overall_count += 1

    print("Over all complete " + str(overall_count))

    if count > 400:
        mycol.insert_many(hadith_batch)
        hadith_batch = []
        count = 0

print("========== COMPLETE ===========")
print("Overall count ", overall_count)
print("UCI end on ", uci.end_on)

mycol.insert_many(hadith_batch)
