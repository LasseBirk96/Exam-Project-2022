"""THIS CLASS CONTAINS ALL API WORK FOR POSTGRES"""
from __main__ import app
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from LogicLayer.ComponentAPI.Handler import Handler


@app.route("/banking", methods=["GET"])
def banking_home():
    """This is just a tester, to see if things are running"""
    return "<h1>THE BANKING API IS RUNNING</h1>"


# PERSISTS A BANK_ACCOUNT
@app.route("/banking", methods=["POST"])
def persist_bank_account():
    """This is the endpoint for persisting a bank account"""
    return Handler.handle_persist_bank_account(data = request.get_json())



# PAYMENT
@app.route("/banking/pay", methods=["POST"])
def payment():
    """This is the endpoint for paying"""
    return Handler.handle_bank_payment(data = request.get_json())

