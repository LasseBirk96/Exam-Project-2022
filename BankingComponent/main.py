"""THIS IS THE MAIN CLASS FROR THE ENTIRE COMPONENT, THIS GETS RUN IN THE DOCKERFILE"""
import sys
import os
from flask import Flask
from flask_restful import Api

sys.path.append("..")
from DatabaseLayer.Setup import postgres_setup


app = Flask(__name__)
api = Api(app)
# THESE ARE NOT TO BE MOVED

from LogicLayer.ComponentAPI import banking_API

@app.route("/home", methods=["GET"])
def home():
    return "<h1>BANKING IS RUNNING</h1>"

if __name__ == "__main__":
    postgres_setup.run_setup()
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
