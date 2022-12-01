"""THIS IS THE MAIN CLASS FROR THE ENTIRE COMPONENT, THIS GETS RUN IN THE DOCKERFILE"""
import sys
import os
from flask import Flask
from flask_restful import Api
from Tests import run_tests
sys.path.append("..")
# from DataBaseLayer.Setup import user_setup
# from Tests import run_tests


app = Flask(__name__)
api = Api(app)
# THESE ARE NOT TO BE MOVED
from LogicLayer.ComponentAPI import order_API

@app.route("/home", methods=["GET"])
def home():
    return "<h1>ORDERS ARE RUNNING</h1>"

if __name__ == "__main__":
    if run_tests.run():
        port = int(os.environ.get("PORT", 5002))
        app.run(debug=False, host="0.0.0.0", port=port)

