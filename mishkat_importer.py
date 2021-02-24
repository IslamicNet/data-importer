######### UCI ###########
# start number: 000000
# end number: 000000
# Book No: 9
#########################
import fireo
import json
from uci import UCI
from models.hadiths.mishkat import Mishkat

mishkat_file = open('./data/hadiths/mishkat.json', "r", encoding="utf8")
mishkat = json.load(mishkat_file)

hadith_batch = fireo.batch()
count = 0
overall_count = 0
uci = UCI(000000)

for hadith in mishkat:
    mishkat = Mishkat()
    mishkat.id = str(hadith['hadees_number'])
    mishkat.hadith_number = int(hadith['hadees_number'])
    mishkat.book_number = int(hadith['Kitab_ID'])
    mishkat.book_name = {
        "urdu": hadith['Kitab'],
        "english": hadith['Kitab_Eng']
    }
    mishkat.chapter = {
        "urdu": hadith['Baab'],
        "english": hadith['Baab_Eng']
    }
    mishkat.text = {
        "arabic": hadith['Arabic'],
        "urdu": hadith['Ravi'] + hadith['Urdu'],
        "english": hadith['English']
    }

    if hadith['Status_Ref'] == '(مُتَّفق عَلَيْهِ)':
        mishkat.grade = {
            "arabic": "مُتَّفق عَلَيْهِ",
            "english": "Muttafaqun alayh"
        }
    else:
        mishkat.grade = {
            "arabic": "صَحِيح",
            "english": "Sahih"
        }

    mishkat.is_sahih = bool(hadith['Sahih_Zaeef'])
    mishkat.uci = uci.next
    mishkat.save(batch=hadith_batch)

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
