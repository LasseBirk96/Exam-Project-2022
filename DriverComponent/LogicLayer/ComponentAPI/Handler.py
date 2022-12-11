from DatabaseLayer.Queries import driver_pg_queries
from DriverLogger.logger_creator import create_logger as log
from LogicLayer.Security import user_jwt
from flask import Flask, request, jsonify
from .HandlerUtility.PointCalculator import PointCalculator

#NEEDS LOGGING
class Handler:
    def __init__(self):
        pass

    def handle_persist_driver(data):
        try:
            driver = driver_pg_queries.persist_driver(
                data.get("first_name"),
                data.get("last_name"),
                data.get("password"),
                data.get("age"),
                data.get("email"),
                data.get("phone_number")
            )
            return jsonify(driver)
        except (Exception) as error:
            log().info(error)
            return "There was an error trying to create your account, please contact the admin"

    def handle_driver_login(data):
        try:
            driver_id = driver_pg_queries.driver_login(
                data.get("email"),
                data.get("password")
            )
            return jsonify(user_jwt.get_access_token(driver_id))
        except (Exception) as error:
            log().info(error)
            return "There was an error trying to log in into your account, please contact the admin"

            
    def handle_driver_points(driver_id):
        points = driver_pg_queries.get_points_by_id(driver_id)
        return jsonify(points)


    def handle_give_points(data):
        points = PointCalculator().calculate_points(data.get("order_id"))
        driver = driver_pg_queries.update_driver_points(points, data.get("driver_id"))

        return jsonify(driver)



