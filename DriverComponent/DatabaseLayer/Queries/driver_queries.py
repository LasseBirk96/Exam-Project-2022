'''THIS CLASS CONTAINS ALL METHODS THAT QUERY THE POSTGRES DATABASE'''
import uuid
from ..Connection.connect_to_postgres import establish_connection
from flask_bcrypt import Bcrypt
from flask import Flask
from LogicLayer.Entities.Driver import Driver
from ..Utility.HashMethods import HashMethods
app = Flask(__name__)
bcrypt = Bcrypt(app)


def persist_driver(first_name, last_name, password, age, email, phone_number):
    '''This method persists a user'''
    driver_id = str(uuid.uuid4())
    hasher = HashMethods()
    hashed_password = hasher.hash_value(password)
    points = 0
    driver = Driver(
        driver_id, first_name, last_name, age, phone_number,  email, hashed_password, points
    )
    persist_driver_query = "INSERT INTO drivers (driver_id, first_name, last_name, age, phonenumber, email, password, points) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    connection = establish_connection()
    cursor = connection.cursor()
    # Execute the tuple with tables
    try:
        cursor.execute(persist_driver_query, driver.return_driver())
        connection.commit()
        return "Success"
    except (Exception) as error:
       return error
    finally:
        if connection is not None:
            connection.close()


def driver_login(driver_email, driver_password):
    '''This method allows the user to log in'''
    connection = establish_connection()
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
        else:
            return "INVALID LOG-IN"
    except (Exception) as error:
       return error
    finally:
        if connection is not None:
            connection.close()



def get_driver_by_id(driver_id):
    '''This allows us to get the driver by their id'''
    conn = establish_connection()
    cur = conn.cursor()
    driver_delete_query = "SELECT * FROM drivers WHERE driver_id = %s"
    try:
        cur.execute(driver_delete_query, (driver_id,))
        driver = cur.fetchall()
        return driver
    except (Exception) as error:
        print("ERROR IN selecting", error)
    finally:
        if conn is not None:
            conn.close()


