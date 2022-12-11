from DatabaseLayer.Queries import product_queries
from LogicLayer.Security.InputSanitizer import InputSanitizer as clean
from ProductLogger.logger_creator import create_logger as log
from flask import Flask, request, jsonify
class Handler:
    def __init__(self):
        pass

    def handle_persist_product(data):
        san = clean()
        if san.clean_input(data):
            try: 
                product = product_queries.persist_product(data.get("product_name"), data.get("description"), data.get("ingredients"), data.get("price"))
                return jsonify(product)
            except (Exception) as error:
                log().info(error)
                return "An error occured whilst trying to create the product, please contact the admin"
        return "Invalid input"
   


    def handle_delete_product(data):
        try:
            product_queries.delete_product(data.get("product_name"))
        except (Exception) as error:
            log().info(error)
            return "An error occured whilst trying to delete the product, please contact the admin"

    
    def handle_get_all_products():
        try:
            products = product_queries.get_products()
        except (Exception) as error:
            log().info(error)
            return "An error occured whilst trying to get the products, please contact the admin"