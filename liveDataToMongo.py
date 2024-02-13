import pymongo
client = pymongo.MongoClient("mongodb+srv://name:password@guvilavan.5pjwpvl.mongodb.net/?retryWrites=true&w=majority")
db = client['newDataBase']
col = db["Datas"]
import requests
import json
collection=db.satelite
import time
for i in range(12):
    iss = requests.get("http://api.open-notify.org/iss-now.json")
    x = iss.text
    y = json.loads(x)
    collection.insert_one(y) 
    time.sleep(3,600)   # 3600 seconds.This loop will take the data for every hours. 
