# data-importer

Python Data importer for Islamic content, import data to Firestore e.g Quran, Hadith or any other kind of data related to Islam

# Local installation

1. Create virtual env `virtualenv venv -p python3`
2. Active virtual env
3. Install UCI `pip install uci`

# For Firestore

1. Install **Fireo** ORM package for Firestore `pip install fireo`

# For MongoDB

1. switch to mongodb branch `git checkout mongodb`
2. install pymongo `pip install pymongo`

# Run importer

1. Start Firestore emulator
   `firebase emulators:start --only firestore --import=./cache --export-on-exit`

2. `export FIRESTORE_EMULATOR_HOST="localhost:8080"` in python terminal
3. run the importer for example `python quran_importer.py`
