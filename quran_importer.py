######### UCI ###########
# start number: 337185
# end number: 343534
#########################
import pymongo
from uci import UCI

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["islamic_content_v1"]
mycol = mydb["quran"]


ar_quran = open('./data/quran/ar.quran_rtl.txt', "r", encoding="utf8")
en_quran = open('./data/quran/en.sahih_ltr.txt', "r", encoding="utf8")
ur_quran = open('./data/quran/ur.maududi_rtl.txt', "r", encoding="utf8")

ayah_batch = []
count = 0
line_count = 0
uci = UCI(337185)

for ar, en, ur in zip(ar_quran, en_quran, ur_quran):

    if not en.strip():
        print('English file end')
        break

    surah_number, ayah_number, en_text = en.strip().split('|')
    _, _, ur_text = ur.strip().split('|')
    _, _, ar_text = ar.strip().split('|')

    print(' writing line...' + str(line_count) + ' ...Surah ' +
          surah_number + ' ...Ayah ' + ayah_number)
    line_count += 1

    docUCI = uci.next

    ayah = {
        "_id": docUCI,
        "uci": docUCI,
        "ayahId": str(surah_number) + '-' + str(ayah_number),
        "number": int(ayah_number),
        "surahNumber": int(surah_number),
        "arabic": ar_text,
        "translations": {
            "urdu": ur_text,
            "english": en_text
        }

    }
    ayah_batch.append(ayah)

    count += 1

    if(count >= 400):
        mycol.insert_many(ayah_batch)
        ayah_batch = []
        count = 0

print('============Complete=============================')
print(uci.end_on)
mycol.insert_many(ayah_batch)
