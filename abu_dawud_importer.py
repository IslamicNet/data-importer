######### UCI ###########
# start number: 362617
# end number: 367891
# Book No: 4
#########################
import fireo
import json
from uci import UCI
from models.hadiths.abudawud import AbuDawud

abudawud_file = open('./data/hadiths/abu_dawud.json', "r", encoding="utf8")
abudawud = json.load(abudawud_file)

hadith_batch = fireo.batch()
count = 0
overall_count = 0
uci = UCI(362617)

for hadith in abudawud:
    abudawud = AbuDawud()
    abudawud.id = str(hadith['hadees_number'])
    abudawud.hadith_number = int(hadith['hadees_number'])
    abudawud.book_number = int(hadith['Kitab_ID'])
    abudawud.book_name = {
        "urdu": hadith['Kitab'],
        "english": hadith['Kitab_Eng']
    }
    abudawud.chapter = {
        "urdu": hadith['Baab'],
        "english": hadith['Baab_Eng']
    }
    abudawud.text = {
        "arabic": hadith['Arabic'],
        "urdu": hadith['Ravi'] + hadith['Urdu'],
        "english": hadith['English']
    }
    abudawud.is_sahih = bool(hadith['Sahih_Zaeef'])
    abudawud.uci = uci.next
    abudawud.save(batch=hadith_batch)

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
