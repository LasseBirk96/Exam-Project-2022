from DatabaseLayer.Queries import bank_account_queries
from LogicLayer.Security.InputSanitizer import InputSanitizer
from BankingLogger.logger_creator import create_logger as log
from flask import Flask, request, jsonify


#NEEDS LOGGING
class Handler:
    def __init__(self):
        pass


    def handle_persist_bank_account(data):
        sanitizer = InputSanitizer()
        if sanitizer.clean_input(data):
            try:
                bank_account = bank_account_queries.persist_bank_account(
                    data.get("email"),
                    data.get("account_number"),
                    data.get("CVV"),
                    data.get("pin_code"),
                    data.get("balance"),
                )
                return jsonify(bank_account)
            except (Exception) as error:
                log().info(error)
                return "Could not create your account"
        return "Invalid input"


    def handle_bank_payment(data):
        sanitizer = InputSanitizer()
        if sanitizer.clean_input(data):
            try: 
                bank_account = bank_account_queries.handle_payment(
                    data.get("email"),
                    data.get("account_number"),
                    data.get("CVV"),
                    data.get("pin_code"),
                    data.get("price")
                )
                return jsonify(bank_account)
            except (Exception) as error:
                log().info(error)
                return "Could not handle payment"
        return "invalid input"