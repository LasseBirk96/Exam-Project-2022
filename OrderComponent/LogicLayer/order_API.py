"""THIS CLASS CONTAINS ALL API WORK FOR POSTGRES"""
from __main__ import app
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from .Entities.Order import Order



@app.route("/order", methods=["GET"])
def order_home():
    """This is just a tester, to see if things are running"""
    return "<h1>THE ORDER API IS RUNNING</h1>"


# PERSISTS A ORDER
@app.route("/order", methods=["POST"])
def persist_order():
    """This is the endpoint for persisting an order"""
    data = request.get_json()
    
    order = Order(
        data.get("email"),
        data.get("delivery_address"),
        data.get("phone_number")
    )
    return jsonify(order)



