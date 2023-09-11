import pymongo
from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:admin@cluster0.tfybhdd.mongodb.net/?retryWrites=true&w=majority")
#collection = db ["students"]
print (db.list_collection_names)