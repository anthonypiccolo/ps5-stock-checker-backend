
import time
import copy
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# local creds
cred = credentials.Certificate("/Users/adam/development/ps5-stock-selector-config/ps5-stock-selector-firebase.json")
firebase_admin.initialize_app(cred)

def throttle_check_store_sku(store_sku):
    """ Will look at the last time we sent a message for the store and then 
    decide if we want to throttle
     """
    db = firestore.client()
    document_ref = db.collection('throttle').document(store_sku)
    print(f"looking for {store_sku}")
    document = document_ref.get().to_dict()
    print(document)
    ouput = document['last_sent']
    
    return ouput

def throttle_update_store_sku(store_sku, time_value=int(time.time()) ):
    """ Will update the store sku timestamp with the latest time
     """
    
    # time_now = int(time.time()) #epoch time int
    db = firestore.client()
    batch = db.batch()

    document_ref = db.collection(u'throttle').document(store_sku)
    batch.update(document_ref, {u'last_sent': time_value})

    batch.commit()

def throttle_dict(input_dict, throttle_time_secs=1200):
    """
    Takes the dictionary of stores which have matches 
    and will see if we're okay to let them through. 
    Will return dict with stores which are okay to send 
    based on the rules we specify in the ENVIRONMENT VARIABLE for 
    THROTTLE_TIME
    Default is 20 mins (1200seconds)
    """
    output_dict = copy.deepcopy(input_dict) #deep copy will allow us to work with this copy uniquely

    for key in input_dict:
        for sku in ["disc","digital"]:
            if input_dict[key][sku] != None and input_dict[key][sku] != "":
                firestore_key = f"{key}_{sku}"
                time_now = int(time.time())
                last_sent = throttle_check_store_sku(firestore_key)
                if time_now < (last_sent + throttle_time_secs):
                    output_dict[key][sku] = None #clear the value since we've sent it recently
                    print(f"We're not going to send an update for {firestore_key} as we notified less than {throttle_time_secs} seconds ago")
                else:
                    throttle_update_store_sku(firestore_key,time_now)

    return output_dict


# print(throttle_check_store_sku("amazon_digital") )