from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["stock_db"]
collection = db["top_stocks"]


def insert_stock_data(data):
    collection.insert_many(data)
