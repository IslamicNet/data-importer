######### UCI ###########
# start number: 343534
# end number: 351097
# Book No: 1
#########################
import fireo
import json
from uci import UCI
from models.hadiths.bukhari import Bukhari

bukhari_file = open('./data/hadiths/bukhari.json', "r", encoding="utf8")
bukhari = json.load(bukhari_file)

hadith_batch = fireo.batch()
count = 0
overall_count = 0
uci = UCI(343534)

for hadith in bukhari:
    bukhari = Bukhari()
    bukhari.id = str(hadith['hadees_number'])
    bukhari.hadith_number = int(hadith['hadees_number'])
    bukhari.book_number = int(hadith['Kitab_ID'])
    bukhari.book_name = {
        "urdu": hadith['Kitab'],
        "english": hadith['Kitab_Eng']
    }
    bukhari.chapter = {
        "urdu": hadith['Baab'],
        "english": hadith['Baab_Eng']
    }
    bukhari.text = {
        "arabic": hadith['Arabic'],
        "urdu": hadith['Ravi'] + hadith['Urdu'],
        "english": hadith['English']
    }
    bukhari.is_sahih = bool(hadith['Sahih_Zaeef'])
    bukhari.uci = uci.next
    bukhari.save(batch=hadith_batch)

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
