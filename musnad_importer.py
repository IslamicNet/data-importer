######### UCI ###########
# start number: 0000000
# end number: 000000
# Book No: 8
#########################
import fireo
import json
from uci import UCI
from models.hadiths.musnad import Musnad

musnad_file = open('./data/hadiths/musnad.json', "r", encoding="utf8")
musnad = json.load(musnad_file)

hadith_batch = fireo.batch()
count = 0
overall_count = 0
uci = UCI(400000)

for hadith in musnad:
    musnad = Musnad()
    musnad.id = str(hadith['hadees_number'])
    musnad.hadith_number = int(hadith['hadees_number'])
    musnad.book_number = int(hadith['Kitab_ID'])
    musnad.book_name = {
        "urdu": hadith['Kitab'],
        "english": hadith['Kitab_Eng']
    }
    musnad.chapter = {
        "urdu": hadith['Baab'],
        "english": hadith['Baab_Eng']
    }
    musnad.text = {
        "arabic": hadith['Arabic'],
        "urdu": hadith['Ravi'] + hadith['Urdu'],
        "english": hadith['English']
    }
    musnad.is_sahih = bool(hadith['Sahih_Zaeef'])
    musnad.uci = uci.next
    musnad.save(batch=hadith_batch)

    count += 1
    overall_count += 1

    print("Over all complete " + str(overall_count))

    if count > 3:
        break
        exit

    if count > 400:
        hadith_batch.commit()
        count = 0

print("========== COMPLETE ===========")
print("Overall count ", overall_count)
print("UCI end on ", uci.end_on)

hadith_batch.commit()
