"""THIS IS THE MAIN CLASS FROR THE ENTIRE COMPONENT, THIS GETS RUN IN THE DOCKERFILE"""
import sys
import os
from flask import Flask
from flask_restful import Api

sys.path.append("..")
from DatabaseLayer.Setup import driver_setup



app = Flask(__name__)
api = Api(app)
# THESE ARE NOT TO BE MOVED
from LogicLayer.ComponentAPI import driver_api

@app.route("/home", methods=["GET"])
def home():
    return "<h1>DRIVERS ARE RUNNING</h1>"
#ADDING A COMMENT
if __name__ == "__main__":
    driver_setup.run_setup()
    port = int(os.environ.get("PORT", 5004))
    app.run(debug=False, host="0.0.0.0", port=port)

