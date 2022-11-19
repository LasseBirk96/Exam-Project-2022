"""THIS CLASS CONTAINS ALL API WORK FOR POSTGRES"""
from __main__ import app
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from DatabaseLayer.Queries import user_queries
from ..Security import user_jwt
from LogicLayer.ComponentAPI.Handler import Handler


# PERSISTS A USER
@app.route("/user", methods=["POST"])
def persist_user():
    """This is the endpoint for persisting a user"""
    return Handler.handle_persist_user(data = request.get_json())

    
@app.route("/user/login", methods=["POST"])
def login_user():
    """This is the endpoint for loggin a user in"""
    return Handler.handle_user_login(data = request.get_json())


@app.route("/user/whoami", methods=["GET"])
def whoami():
    '''This endpoint returns the data of a logged in user'''
    if not request.headers.has_key("Authorization"):
        return jsonify({"error": "You are not authorized"})
    bearer = request.headers.get("Authorization")
    token = bearer[len("Bearer ") :]
    decoded = user_jwt.decode_access_token(token)
    user = user_queries.get_user_by_id(decoded["sub"])
    return jsonify(user)


    
