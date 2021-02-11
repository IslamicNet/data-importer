# data-importer
Python Data importer for Islamic content, import data to Firestore e.g Quran, Hadith or any other kind of data related to Islam

# Local installation

1. Create virtual env `virtualenv -venv -p python3`
2. Active virtual env
3. Install **Fireo** ORM package for Firestore `pip install fireo`

# Run importer
1. Start Firestore emulator 
`firebase emulators:start --only firestore --import=./cache --export-on-exit`

2. `export FIRESTORE_EMULATOR_HOST="localhost:8080"` in python terminal
3. run the importer for example `python quran_importer.py`