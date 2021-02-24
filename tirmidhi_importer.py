######### UCI ###########
# start number: 358661
# end number: 362617
# Book No: 3
#########################
import fireo
import json
from uci import UCI
from models.hadiths.tirmidhi import Tirmidhi

tirmidhi_file = open('./data/hadiths/tirmidhi.json', "r", encoding="utf8")
tirmidhi = json.load(tirmidhi_file)

hadith_batch = fireo.batch()
count = 0
overall_count = 0
uci = UCI(358661)

for hadith in tirmidhi:
    tirmidhi = Tirmidhi()
    tirmidhi.id = str(hadith['hadees_number'])
    tirmidhi.hadith_number = int(hadith['hadees_number'])
    tirmidhi.book_number = int(hadith['Kitab_ID'])
    tirmidhi.book_name = {
        "urdu": hadith['Kitab'],
        "english": hadith['Kitab_Eng']
    }
    tirmidhi.chapter = {
        "urdu": hadith['Baab'],
        "english": hadith['Baab_Eng']
    }
    tirmidhi.text = {
        "arabic": hadith['Arabic'],
        "urdu": hadith['Ravi'] + hadith['Urdu'],
        "english": hadith['English']
    }
    tirmidhi.is_sahih = bool(hadith['Sahih_Zaeef'])
    tirmidhi.uci = uci.next
    tirmidhi.save(batch=hadith_batch)

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
