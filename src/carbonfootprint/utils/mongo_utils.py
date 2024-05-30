from pymongo import MongoClient

def connect_to_mongodb(uri, db_name):
    client = MongoClient(uri)
    db = client[db_name]
    return db