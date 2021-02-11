from os import listdir
from os.path import isfile, join

import fireo
from models.quran.ayah import Ayah

ar_quran = open('./data/quran/ar.quran_rtl.txt', "r", encoding="utf8")
en_quran = open('./data/quran/en.sahih_ltr.txt', "r", encoding="utf8")
ur_quran = open('./data/quran/ur.maududi_rtl.txt', "r", encoding="utf8")

ayah_batch = fireo.batch()
count = 0
line_count = 0

for ar, en, ur in zip(ar_quran, en_quran, ur_quran):
    
    if not en.strip():
        print('English file end')
        break

    surah_number, ayah_number, en_text = en.strip().split('|')
    _, _, ur_text = ur.strip().split('|')
    _, _, ar_text = ar.strip().split('|')

    print(' writing line...' + str(line_count) + ' ...Surah ' + surah_number + ' ...Ayah ' + ayah_number)
    line_count += 1

    ayah = Ayah()
    ayah.id = str(surah_number) + '-' + str(ayah_number)
    ayah.number = int(ayah_number)
    ayah.surah_number = int(surah_number)
    ayah.content = {
        "arabic": {
            "text": ar_text,
            "direction": "rtl"
        },
        "english": {
            "text": en_text,
            "direction": "ltr"
        },
        "urdu": {
            "text": ur_text,
            "direction": "rtl"
        },
    }
    ayah.save(batch=ayah_batch)

    count += 1

    if(count >= 400):
        ayah_batch.commit()
        count = 0

print('============Complete=============================')
ayah_batch.commit()