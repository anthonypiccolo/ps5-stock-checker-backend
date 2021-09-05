# only run this once to reset stuff or setup stuff

import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# from dotenv import load_dotenv
# load_dotenv()

# local creds
cred = credentials.Certificate("/Users/adam/development/ps5-stock-selector-config/ps5-stock-selector-firebase.json")
firebase_admin.initialize_app(cred)

# Use the application default credentials
# cred = credentials.ApplicationDefault()
# firebase_admin.initialize_app(cred, {
#   'projectId': 'ps5-stock-selector',
# })

db = firestore.client()

### initialize collection ###

#throttle structure:
# Collection: 'throttle'
# Document: <store>_<sku>
# fields: last_sent (timestamp)

to_initialize = [
    u"target_digital",
    u"target_disc",
    u"bigw_digital",
    u"bigw_disc",
    u"amazon_digital",
    u"amazon_disc"
]

for each_item in to_initialize:
    doc_ref = db.collection(u'throttle').document(each_item)
    doc_ref.set({
        u'last_sent': int(time.time())
    })

print("Completed initialization. You should now have populated docs in your firestore")