import os
from pymongo import MongoClient

def connect_to_collection(collection_):
    """This establishes connection to our mongo db."""
    host = os.environ.get("MONGO_HOST")
    user = os.environ.get("MONGO_USER")
    password = os.environ.get("MONGO_PASSWORD")
    port = os.environ.get("MONGO_PORT")

    dsn = f"mongodb://{user}:{password}@{host}:{port}/?authMechanism=DEFAULT"

    client = MongoClient(dsn, uuidRepresentation="standard")
    database = client["Exam2022"]
    collection = database[collection_]
    return collection



