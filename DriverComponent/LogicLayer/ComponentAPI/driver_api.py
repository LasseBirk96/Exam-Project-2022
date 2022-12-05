"""THIS CLASS CONTAINS ALL API WORK FOR POSTGRES"""
from __main__ import app
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from LogicLayer.ComponentAPI.Handler import Handler


# PERSISTS A DRIVER
@app.route("/driver", methods=["POST"])
def persist_driver():
    """This is the endpoint for persisting a driver"""
    return Handler.handle_persist_driver(data = request.get_json())


@app.route("/driver/login", methods=["POST"])
def login_driver():
    """This is the endpoint for loggin a driver in"""
    return Handler.handle_driver_login(data = request.get_json())
