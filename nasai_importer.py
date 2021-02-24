######### UCI ###########
# start number: 367891
# end number: 373652
# Book No: 5
#########################
import fireo
import json
from uci import UCI
from models.hadiths.nasai import Nasai

nasai_file = open('./data/hadiths/nasai.json', "r", encoding="utf8")
nasai = json.load(nasai_file)

hadith_batch = fireo.batch()
count = 0
overall_count = 0
uci = UCI(367891)

for hadith in nasai:
    nasai = Nasai()
    nasai.id = str(hadith['hadees_number'])
    nasai.hadith_number = int(hadith['hadees_number'])
    nasai.book_number = int(hadith['Kitab_ID'])
    nasai.book_name = {
        "urdu": hadith['Kitab'],
        "english": hadith['Kitab_Eng']
    }
    nasai.chapter = {
        "urdu": hadith['Baab'],
        "english": hadith['Baab_Eng']
    }
    nasai.text = {
        "arabic": hadith['Arabic'],
        "urdu": hadith['Ravi'] + hadith['Urdu'],
        "english": hadith['English']
    }
    nasai.is_sahih = bool(hadith['Sahih_Zaeef'])
    nasai.uci = uci.next
    nasai.save(batch=hadith_batch)

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
