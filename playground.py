import os
import firebase_admin
import json
import irmcli
import datetime
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate(os.path.join("secret_key","daicon-credentials.json"))
firebase_admin.initialize_app(cred)

"""
trainingList = ["縄跳び", "背筋", "腹筋", "腕立て", "スクワット"]
training = "腕立て"
count = 0"""

"""
date = datetime.datetime.now()
year = str(date.year)
month = "{:02d}".format(date.month)
day = "{:02d}".format(date.day)
"""

#date2str = year+month+day

db = firestore.client()
doc_ref = db.collection('TV').get()

log_json = {}
for doc in doc_ref:
    print(doc.id, doc.to_dict())
    log_json[str(doc.id)] = doc.to_dict()
    

#print(log_json)
#print("------------------------")
"""set_dict = {
    trainingList[0]: 31,
    trainingList[1]: 10,
    trainingList[2]: 44,
    trainingList[3]: 35,
    trainingList[4]: 11,
    'date': int(date2str)
}"""
#print(log_json[date2str])

#log_json[date2str][training] += count

#print(log_json[date2str])

#print(db.collection('log').get())
#doc_ref_ = db.collection('log').document(date2str)
#doc_ref_.set(log_json[date2str])

detail = "DUMMY"
a = [1,2,3,4]

set_json = {
    "signal": " ".join(map(str,a))
    }
            
#target_ref = db.collection('TV_signal').document(detail)           
#target_ref.set(set_json)
