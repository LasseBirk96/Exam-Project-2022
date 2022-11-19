from DatabaseLayer.Connection import connector
from DatabaseLayer.Queries import order_queries

class Handler:

    def __init__(self):
        pass

    def handle_order_creation(data):
        list_of_products = []
        for element in data.get("products"):
            product = {"name":element.get("name"), "price":element.get("price")}
            list_of_products.append(product.return_product())
        return order_queries.insert_order(connector.connect_to_collection("Order"),  list_of_products)

 
