"""THIS CLASS CONTAINS ALL API WORK FOR POSTGRES"""
from __main__ import app
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from DataBaseLayer.Queries import user_queries
from .Security.InputSanitizer import InputSanitizer


# PERSISTS A USER
@app.route("/user", methods=["POST"])
def persist_user():
    """This is the endpoint for persisting a user"""
    data = request.get_json()
    sanitizer = InputSanitizer()
    if sanitizer.clean_input(data):
        user = user_queries.persist_user(
            data.get("first_name"),
            data.get("last_name"),
            data.get("password"),
            data.get("age"),
            data.get("email"),
            data.get("phone_number")
        )
        return jsonify(user)
    return "Invalid input"
    

@app.route("/user/login", methods=["POST"])
def login_user():
    """This is the endpoint for loggin a user in"""
    data = request.get_json()
    sanitizer = InputSanitizer()
    if sanitizer.clean_input(data):
        user = user_queries.user_login(
            data.get("email"),
            data.get("password")
        )
        return jsonify(user)
    return "Invalid input"
