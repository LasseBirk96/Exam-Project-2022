"""THIS CLASS CONTAINS ALL API WORK FOR POSTGRES"""
from __main__ import app
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from DataBaseLayer.Queries import bank_account_queries


@app.route("/banking", methods=["GET"])
def banking_home():
    """This is just a tester, to see if things are running"""
    return "<h1>THE BANKING API IS RUNNING</h1>"


# PERSISTS A BANK_ACCOUNT
@app.route("/banking", methods=["POST"])
def persist_bank_account():
    """This is the endpoint for persisting a user"""
    data = request.get_json()
    bank_account = bank_account_queries.persist_bank_account(
        data.get("email"),
        data.get("account_number"),
        data.get("CVV"),
        data.get("pin_code"),
        data.get("balance"),
    )
    return jsonify(bank_account)


# PAYMENT
@app.route("/banking/pay", methods=["POST"])
def payment():
    """This is the endpoint for paying"""
    data = request.get_json()
    bank_account = bank_account_queries.handle_payment(
        data.get("email"),
        data.get("account_number"),
        data.get("CVV"),
        data.get("pin_code"),
        data.get("price")
    )
    return jsonify(bank_account)
