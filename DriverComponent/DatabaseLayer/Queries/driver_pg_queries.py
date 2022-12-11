'''THIS CLASS CONTAINS ALL METHODS THAT QUERY THE POSTGRES DATABASE'''
import uuid
from LogicLayer.Entities.Driver import Driver
from ..Utility.HashMethods import HashMethods
from DatabaseLayer.Connection import connect_to_postgres
from flask_bcrypt import Bcrypt
from flask import Flask

app = Flask(__name__)
bcrypt = Bcrypt(app)


def persist_driver(first_name, last_name, password, age, email, phone_number, connection = None):
    '''This method persists a user'''
    if connection == None:
        connection = connect_to_postgres.establish_connection()
    driver_id = str(uuid.uuid4())
    hasher = HashMethods()
    hashed_password = hasher.hash_value(password)
    points = 0
    driver = Driver(
        driver_id, first_name, last_name, age, phone_number,  email, hashed_password, points
    )
    persist_driver_query = "INSERT INTO drivers (driver_id, first_name, last_name, age, phonenumber, email, password, points) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor = connection.cursor()
    try:
        cursor.execute(persist_driver_query, driver.return_driver())
        print(driver.return_driver())
        connection.commit()
        return driver_id
    except (Exception) as error:
       return error



def driver_login(driver_email, driver_password, connection = None):
    '''This method allows the user to log in'''
    if connection == None:
        connection = connect_to_postgres.establish_connection()
    cursor = connection.cursor()
    login_query = "SELECT driver_id, password FROM drivers WHERE email = %s"
    try:
        cursor.execute(login_query, (driver_email,))
        entries = cursor.fetchall()[0]
        sql_data_password = entries[1]
        hasher = HashMethods()
        if hasher.check_hashed_value(driver_password, sql_data_password):
            print(type(entries[0]))
            return entries[0]
    except (Exception) as error:
       return error



def get_driver_by_id(driver_id, connection = None):
    if connection == None:
        connection = connect_to_postgres.establish_connection()
    '''This allows us to get the driver by their id'''
    
    cur = connection.cursor()
    driver_delete_query = "SELECT * FROM drivers WHERE driver_id = %s"
    try:
        cur.execute(driver_delete_query, (driver_id,))
        driver = cur.fetchall()
        return driver
    except (Exception) as error:
        print("ERROR IN selecting", error)


def get_points_by_id(driver_id, connection = None):
    if connection == None:
        connection = connect_to_postgres.establish_connection()
    cursor = connection.cursor()
    get_points_query = "SELECT points FROM drivers where driver_id = %s"
    try:
        cursor.execute(get_points_query, (driver_id,))
        driver = cursor.fetchall()[0]
        return driver[0]
    except (Exception) as error:
        print("ERROR IN selecting", error)
    finally:
        if connection is not None:
            connection.close()


def update_driver_points(driver_id, points, current_points, connection = None):
    if connection == None:
        connection = connect_to_postgres.establish_connection()
    new_total = current_points + points
    cursor = connection.cursor()
    update_points_query = "UPDATE drivers SET points = %s where driver_id = %s"
    try: 
        cursor.execute(update_points_query, (new_total, driver_id))
        connection.commit()
        return new_total
    except (Exception) as error:
        print("ERROR IN selecting", error)
    finally:
        if connection is not None:
            connection.close()

