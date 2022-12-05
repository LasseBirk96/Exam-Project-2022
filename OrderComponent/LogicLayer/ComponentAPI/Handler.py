from DatabaseLayer.Connection import connector
from DatabaseLayer.Queries import order_queries
from ..Utility.GoogleAPI import GoogleAPI
import uuid
class Handler:

    def __init__(self):
        pass

    def handle_order_creation(data):
        delivery_information = GoogleAPI().get_delivery_information(data.get("deliveryAddress"), data.get("resturantAddress"), data.get("products"))
        data.update({"delivery_information":delivery_information})
        data.update({"order_id": str(uuid.uuid4())})
        order_queries.insert_order(connector.connect_to_collection(), data)
        return "Order confirmation has been send to your email <3"

 
