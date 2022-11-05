"""THIS IS THE MAIN CLASS FROR THE ENTIRE PROJECT, THIS GETS RUN IN THE DOCKERFILE"""
import sys
import os
from flask import Flask
from flask_restful import Api

sys.path.append("..")
from DataBaseLayer.Setup import postgres_setup
from Tests import test_bank_account_queries


app = Flask(__name__)
api = Api(app)
# THESE ARE NOT TO BE MOVED

from LogicLayer import banking_API


@app.route("/home", methods=["GET"])
def home():
    return "<h1>HVIS DU SER DETTE SÅ KØRER DET</h1>"


if __name__ == "__main__":
    postgres_setup.run_setup()
    if test_bank_account_queries.run_tests():
        port = int(os.environ.get("PORT", 5000))
        app.run(debug=False, host="0.0.0.0", port=port)
