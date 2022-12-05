from DatabaseLayer.Queries import driver_queries
from DriverLogger.logger_creator import create_logger as log
from LogicLayer.Security import user_jwt
from flask import Flask, request, jsonify


#NEEDS LOGGING
class Handler:
    def __init__(self):
        pass

    def handle_persist_driver(data):
            driver = driver_queries.persist_driver(
                data.get("first_name"),
                data.get("last_name"),
                data.get("password"),
                data.get("age"),
                data.get("email"),
                data.get("phone_number")
            )
            return jsonify(driver)
 

    def handle_driver_login(data):
            driver_id = driver_queries.driver_login(
                data.get("email"),
                data.get("password")
            )
            return jsonify(user_jwt.get_access_token(driver_id))

