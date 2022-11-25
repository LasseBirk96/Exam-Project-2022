"""THIS CLASS CONTAINS ALL API WORK FOR ORDERS"""
from __main__ import app
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from LogicLayer.ComponentAPI.Handler import Handler


@app.route("/order", methods=["GET"])
def order_home():
    """This is just a tester, to see if things are running"""
    return "<h1>THE ORDER API IS RUNNING</h1>"


# CREATES AN ORDER
@app.route("/order/create", methods=["POST"])
def create_order():
    """This receives data from an api call, and allows you to persist order in mongo"""
    return Handler.handle_order_creation(data = request.get_json())
    


