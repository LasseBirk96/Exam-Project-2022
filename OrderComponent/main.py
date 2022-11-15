"""THIS IS THE MAIN CLASS FROR THE ENTIRE PROJECT, THIS GETS RUN IN THE DOCKERFILE"""
import sys
import os
from flask import Flask
from flask_restful import Api

sys.path.append("..")
# from DataBaseLayer.Setup import user_setup
# from Tests import run_tests


app = Flask(__name__)
api = Api(app)
# THESE ARE NOT TO BE MOVED
from LogicLayer import order_API

@app.route("/home", methods=["GET"])
def home():
    return "<h1>ORDERS ARE RUNNING</h1>"

if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5002))
        app.run(debug=False, host="0.0.0.0", port=port)



# from LogicLayer.GoogleAPI import GoogleAPI


# google_api = GoogleAPI()


# print(google_api.get_delivery_information("Melissehaven 60b, Herlev", "Syvendehusvej 65a, Herlev"))
