import uuid
import json
from LogicLayer.Entities.Order import Order




def insert_order(collection, products):
    """This inserts an order, it requires a collection,
    id of the user who is creating the order, and what products are in the order."""
    test_myuuid1 = uuid.uuid4()
    order = Order(1)
    collection.insert_one(order.return_order())
    return "Succesfully created order"


def get_orders(collection, user_id):
    """This get all orders made by a user, it requires a collection and a user_id."""
    retrieved_data = collection.find_one({"user_id": user_id})
    data = json.dumps(str(retrieved_data))
    return data


def delete_order(collection, order_id):
    """The deletes an order. It requires a collection and the id of the order to be deleted."""
    collection.delete_one({"order_id": order_id})
    return "Successfully deleted order " + order_id


def update_order(collection, order_id, item, new_value):
    """This updates an order, it requires a collection,
    order_id of the order to be deleted,
    the item to be updated, and the new value"""
    collection.update({"order_id": order_id}, {"$set": {item: new_value}})
    return "Successfully updated order " + order_id