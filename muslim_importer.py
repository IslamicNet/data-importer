######### UCI ###########
# start number: 351097
# end number: 358661
# Book No: 2
#########################
import fireo
import json
from uci import UCI
from models.hadiths.muslim import Muslim

muslim_file = open('./data/hadiths/muslim.json', "r", encoding="utf8")
muslim = json.load(muslim_file)

hadith_batch = fireo.batch()
count = 0
overall_count = 0
uci = UCI(351097)

for hadith in muslim:
    muslim = Muslim()
    muslim.id = str(hadith['hadees_number'])
    muslim.hadith_number = int(hadith['hadees_number'])
    muslim.international_number = int(hadith['internationalNumber'])
    muslim.book_number = int(hadith['Kitab_ID'])
    muslim.book_name = {
        "urdu": hadith['Kitab'],
        "english": hadith['Kitab_Eng']
    }
    muslim.chapter = {
        "urdu": hadith['Baab'],
        "english": hadith['Baab_Eng']
    }

    ravi = ""
    if hadith['Ravi']:
        ravi = hadith['Ravi']

    muslim.text = {
        "arabic": hadith['Arabic'],
        "urdu": ravi + hadith['Urdu'],
        "english": hadith['English']
    }
    muslim.is_sahih = bool(hadith['Sahih_Zaeef'])
    muslim.uci = uci.next
    muslim.save(batch=hadith_batch)

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
