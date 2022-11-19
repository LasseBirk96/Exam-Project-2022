"""THIS CLASS CONTAINS ALL API WORK FOR POSTGRES"""
from __main__ import app
from flask import request
from LogicLayer.ComponentAPI.Handler import Handler


@app.route("/product", methods=["GET"])
def product_home():
    """This is just a tester, to see if things are running"""
    return "<h1>THE ORDER API IS RUNNING</h1>"


# CREATES A product
@app.route("/product", methods=["POST"])
def create_product():
    """This receives data from an api call, and allows you to persist a product in postgres"""
    return Handler.handle_persist_product(data = request.get_json())
    

@app.route("/product", methods=["DELETE"])
def delete_product():
    """This receives data from an api call, and allows you to delete product in postgres"""
    return Handler.handle_delete_product(data = request.get_json())


@app.route("/product/all", methods=["GET"])
def get_products():
    """This receives data from an api call, and allows you fetch all products in postgres"""
    return Handler.handle_get_all_products()

