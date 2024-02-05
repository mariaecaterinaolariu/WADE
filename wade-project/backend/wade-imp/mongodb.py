import json
# Checking the database before deploying in cloud
# with open('portraits.json', 'r') as f:
#     data = json.load(f)

# # Check if the data is of format for mongoimport
# # mongoimport only accepts a list of JSON objects or one json object per line
# if not data:
#     print("Data is empty")

# if not isinstance(data, list):
#     print("Data is not a list of JSON objects")
# if not all(isinstance(item, dict) for item in data):
#     print("Not all items in the list are JSON objects")

# with open('portraits.json', 'w') as f:
#     json.dump(data, f)

# TO MAKE IT WORK IN CASE OF ERRORS: 
# py -m pip install httpcore si py -m pip install --upgrade httpcore
# py -m pip install -U httpcore httpx
# Deployed database in cloud using MongoDB Atlas
from pymongo import MongoClient
#password = str(input("Enter password: "))
#connString = "mongodb+srv://mario:"+password+"@cluster.mjrpazd.mongodb.net/"
#client = MongoClient(connString)
# db = client['wade']
# collection_name = 'painters'
# collection = db[collection_name]
# for doc in collection.find():
#     if 'painter' in doc:
#         print(doc['painter'])


def add_entity_to_collection(collection_name, new_entity):
    password = "."
    connString = "mongodb+srv://mario:"+password+"@cluster.mjrpazd.mongodb.net/"
    client = MongoClient(connString)
    db = client['wade']
    collection = db[collection_name]
    result = collection.insert_one(new_entity)
    if(result.acknowledged):
        print('Acknowledged insertion operation')
    print('Inserted entity with ID:', result.inserted_id)

def get_painter_entity_from_collection(name): #name is of format Achille_Beltrame
    password = "."
    connString = "mongodb+srv://mario:"+password+"@cluster.mjrpazd.mongodb.net/"
    client = MongoClient(connString)
    db = client['wade']
    collection = db['painters']
    painter = collection.find_one({'painter': name})
    return painter

def get_portrait_entity_from_collection(name): #name is of format Achille_Beltrame_0001.jpg
    password = "."
    connString = "mongodb+srv://mario:"+password+"@cluster.mjrpazd.mongodb.net/"
    client = MongoClient(connString)
    db = client['wade']
    collection = db['portraits']
    portrait = collection.find_one({'filename': name})

    return portrait
