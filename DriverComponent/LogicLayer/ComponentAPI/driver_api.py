"""THIS CLASS CONTAINS ALL API WORK FOR POSTGRES"""
from __main__ import app
from flask import Flask, request, jsonify, session
from flask_restful import Resource, Api, reqparse
from functools import wraps
from LogicLayer.ComponentAPI.Handler import Handler
from ..Security import user_jwt

app.secret_key = "super secret key"


def requires_user(_f):
    """This allows you to lock other actions behind a JWT token"""

    @wraps(_f)
    def wrapper(*args, **kwargs):
        if not request.headers.has_key("Authorization"):
            print("does not have header")
            return jsonify({"error": "You are not authorized"})

        bearer = request.headers.get("Authorization")
        token = bearer[len("Bearer ") :]

        try:
            decoded = user_jwt.decode_access_token(token)
            session["user_id"] = decoded["sub"]
        except Exception as _e:
            print(_e)
            return jsonify({"error": "You are not authorized"})

        return _f(*args, **kwargs)

    return wrapper


# PERSISTS A DRIVER
@app.route("/driver", methods=["POST"])
def persist_driver():
    """This is the endpoint for persisting a driver"""
    return Handler.handle_persist_driver(data = request.get_json())


@app.route("/driver/login", methods=["POST"])
def login_driver():
    """This is the endpoint for loggin a driver in"""
    return Handler.handle_driver_login(data = request.get_json())


@app.route("/driver/points", methods=["GET"])
@requires_user
def get_driver_points():
    return Handler.handle_driver_points(driver_id = session.get("user_id"))


@app.route("/driver/give", methods=["POST"])
def give_points_based_on_order():
    return Handler.handle_give_points(data = request.get_json())