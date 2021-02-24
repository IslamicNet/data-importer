######### UCI ###########
# start number: 377993
# end number: 000000
# Book No: 7
#########################
import fireo
import json
from uci import UCI
from models.hadiths.sahiha import Sahiha

sahiha_file = open('./data/hadiths/sahiha.json', "r", encoding="utf8")
sahiha = json.load(sahiha_file)

hadith_batch = fireo.batch()
count = 0
overall_count = 0
uci = UCI(377993)

for hadith in sahiha:
    sahiha = Sahiha()
    sahiha.id = str(hadith['hadees_number'])
    sahiha.hadith_number = int(hadith['hadees_number'])
    sahiha.book_number = int(hadith['Kitab_ID'])
    sahiha.book_name = {
        "urdu": hadith['Kitab'],
        "english": hadith['Kitab_Eng']
    }
    sahiha.chapter = {
        "urdu": hadith['Baab'],
        "english": hadith['Baab_Eng']
    }
    sahiha.text = {
        "arabic": hadith['Arabic'],
        "urdu": hadith['Urdu'],
        "english": hadith['English']
    }
    sahiha.is_sahih = bool(hadith['Sahih_Zaeef'])
    sahiha.uci = uci.next
    sahiha.save(batch=hadith_batch)

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
