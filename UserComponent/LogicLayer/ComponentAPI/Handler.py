from DatabaseLayer.Queries import user_queries
from LogicLayer.Security.InputSanitizer import InputSanitizer
from LogicLayer.Security import user_jwt
from UserLogger.logger_creator import create_logger as log
from flask import Flask, request, jsonify


# NEEDS LOGGING
class Handler:
    def __init__(self):
        pass

    def handle_persist_user(data):
        sanitizer = InputSanitizer()
        if sanitizer.clean_input(data):
            try:
                user = user_queries.persist_user(
                    data.get("first_name"),
                    data.get("last_name"),
                    data.get("password"),
                    data.get("age"),
                    data.get("email"),
                    data.get("phone_number"),
                )
                return jsonify(user)
            except (Exception) as error:
                log().info(error)
                return "An error occured whilst trying to create your account, please contact the admin"
        return "Invalid input"

    def handle_user_login(data):
        sanitizer = InputSanitizer()
        if sanitizer.clean_input(data):
            try:
                user_id = user_queries.user_login(
                    data.get("email"), data.get("password")
                )
                return jsonify(user_jwt.get_access_token(user_id))
            except (Exception) as error:
                log().info(error)
                return (
                    "An error occured whilst trying to log in, please contact the admin"
                )
        return "Invalid input"
