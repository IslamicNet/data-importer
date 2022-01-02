######### UCI ###########
# start number: 000000
# end number: 000000
# Book No: 9
#########################
import pymongo
import json
from uci import UCI

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["islamic_content_v1"]
mycol = mydb["mishkat"]

mishkat_file = open('./data/hadiths/mishkat.json', "r", encoding="utf8")
mishkat = json.load(mishkat_file)

hadith_batch = []
count = 0
overall_count = 0
uci = UCI(400000)

for hadith in mishkat:
    docUCI = uci.next
    mishkat = {
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

    if hadith['Status_Ref'] == '(مُتَّفق عَلَيْهِ)':
        mishkat["is_muttafaqun_alayh"] = True
    else:
        mishkat["is_muttafaqun_alayh"] = False

    hadith_batch.append(mishkat)

    print("Over all complete " + str(overall_count))

    if count > 400:
        mycol.insert_many(hadith_batch)
        hadith_batch = []
        count = 0

print("========== COMPLETE ===========")
print("Overall count ", overall_count)
print("UCI end on ", uci.end_on)

mycol.insert_many(hadith_batch)
