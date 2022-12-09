import json
from ..Connection.connect_to_mongo import connect_to_collection

def insert_order(data):
    collection = connect_to_collection("active orders")
    collection.insert_one(data)
    return "Succesfully created order"


def get_order(order_id):
    collection = connect_to_collection("active orders")
    retrieved_data = collection.find_one({"order_id": order_id})
    return retrieved_data


def delete_order(order_id):
    collection = connect_to_collection("active orders")
    collection.delete_one({"order_id": order_id})
    return "Successfully deleted order " + order_id
