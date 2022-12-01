
from DriverLogger.logger_creator import create_logger as log
from flask import Flask, request, jsonify


#NEEDS LOGGING
class Handler:
    def __init__(self):
        pass

    def handle_persist_driver(data):
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


    def handle_driver_login(data):
        sanitizer = InputSanitizer()
        if sanitizer.clean_input(data):
            driver_id = user_queries.user_login(
                data.get("email"),
                data.get("password")
            )
            return jsonify(user_jwt.get_access_token(driver_id))
        return "Invalid input"
