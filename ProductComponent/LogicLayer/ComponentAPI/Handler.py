from DatabaseLayer.Queries import product_queries
from LogicLayer.Security.InputSanitizer import InputSanitizer as clean
from ProductLogger.logger_creator import create_logger as log

class Handler:
    def __init__(self):
        pass

    def handle_persist_product(data):
        san = clean()
        #THE SANITIZER SHOULD WORK BUT IT DOESN'T IDK WHAT IS GOING ON???
        if san.clean_input(data):
            product_queries.persist_product(data.get("product_name"), data.get("description"), data.get("ingredients"), data.get("price"))
            log().info("Persisted product: " + data.get("product_name"))
            return "Success"
        log().error("Could not persist product: " + data.get("product_name"))
        return "Failure"

    def handle_delete_product(data):
        product_queries.delete_product(data.get("product_name"))
        log().info("Deleted product: " + data.get("product_name"))
        return "Success"

    
    def handle_get_all_products():
        products = product_queries.get_products()
        log().info("Got all products")
        return products