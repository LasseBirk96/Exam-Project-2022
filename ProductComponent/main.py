"""THIS IS THE MAIN CLASS FROR THE ENTIRE PROJECT, THIS GETS RUN IN THE DOCKERFILE"""
import sys
import os
from flask import Flask
from flask_restful import Api
from DatabaseLayer.Setup import products_setup
sys.path.append("..")
# from DataBaseLayer.Setup import user_setup
# from Tests import run_tests


app = Flask(__name__)
api = Api(app)
# THESE ARE NOT TO BE MOVED


@app.route("/home", methods=["GET"])
def home():
    return "<h1>PRODUCTS ARE RUNNING</h1>"

if __name__ == "__main__":
        products_setup.run_setup()
        port = int(os.environ.get("PORT", 5003))
        app.run(debug=False, host="0.0.0.0", port=port)


