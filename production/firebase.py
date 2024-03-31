import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# add the cred
def connect_firestore(path, collection_name):

    cred = credentials.Certificate(path)
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    #doc_ref = db.collection(collection_name).document()

    return db

# define the collection name that will be stored



