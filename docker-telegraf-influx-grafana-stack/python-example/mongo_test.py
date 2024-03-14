from pymongo import MongoClient

try:
    conn = MongoClient()
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

# database 
db = conn.database

# Created or Switched to collection names: my_gfg_collection 
collection = db.my_gfg_collection

for i in range(1, 1000000):
    emp_rec = {
        "name": "Mr" + str(i),
        "eid": i,
        "location": "Kyiv"
    }
    rec_id = collection.insert_one(emp_rec)
    print("Data inserted with record ids", rec_id)
