######### UCI ###########
# start number: 373652
# end number: 377993
# Book No: 6
#########################
import fireo
import json
from uci import UCI
from models.hadiths.ibnemaja import IbneMaja

ibnemaja_file = open('./data/hadiths/ibne_maja.json', "r", encoding="utf8")
ibnemaja = json.load(ibnemaja_file)

hadith_batch = fireo.batch()
count = 0
overall_count = 0
uci = UCI(373652)

for hadith in ibnemaja:
    ibnemaja = IbneMaja()
    ibnemaja.id = str(hadith['hadees_number'])
    ibnemaja.hadith_number = int(hadith['hadees_number'])
    ibnemaja.book_number = int(hadith['Kitab_ID'])
    ibnemaja.book_name = {
        "urdu": hadith['Kitab'],
        "english": hadith['Kitab_Eng']
    }
    ibnemaja.chapter = {
        "urdu": hadith['Baab'],
        "english": hadith['Baab_Eng']
    }
    ibnemaja.text = {
        "arabic": hadith['Arabic'],
        "urdu": hadith['Ravi'] + hadith['Urdu'],
        "english": hadith['English']
    }
    ibnemaja.is_sahih = bool(hadith['Sahih_Zaeef'])
    ibnemaja.uci = uci.next
    ibnemaja.save(batch=hadith_batch)

    count += 1
    overall_count += 1

    print("Over all complete " + str(overall_count))

    if count > 400:
        hadith_batch.commit()
        count = 0

print("========== COMPLETE ===========")
print("Overall count ", overall_count)
print("UCI end on ", uci.end_on)

hadith_batch.commit()
