'''THIS CLASS CONTAINS ALL METHODS THAT QUERY THE POSTGRES DATABASE'''
import random
from ..Connection.connector import establish_connection
from flask_bcrypt import Bcrypt
from flask import Flask
from LogicLayer.Entities.Driver import Driver
from ..Utility.HashMethods import HashMethods
app = Flask(__name__)
bcrypt = Bcrypt(app)


def persist_driver(first_name, last_name, password, age, email, phone_number):
    '''This method persists a driver'''
    driver_id = random.randint(0000,9999)
    hasher = HashMethods()
    hashed_password = hasher.hash_value(password)
    driver = Driver(
        driver_id, first_name, last_name, hashed_password, age, email, phone_number
    )
    persist_driver_query = "INSERT INTO drivers (driver_id, first_name, last_name, password, age, email, phonenumber) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    connection = establish_connection()
    cursor = connection.cursor()
    # Execute the tuple with tables
    try:
        cursor.execute(persist_driver_query, driver.return_user())
        connection.commit()
        return "Success"
    except (Exception) as error:
       return error
    finally:
        if connection is not None:
            connection.close()


# def user_login(user_email, user_password):
#     '''This method allows the user to log in'''
#     connection = establish_connection()
#     cursor = connection.cursor()
#     user_login_query = "SELECT user_id, password FROM users WHERE email = %s"
#     try:
#         cursor.execute(user_login_query, (user_email,))
#         entries = cursor.fetchall()[0]
#         sql_data_password = entries[1]
#         hasher = HashMethods()
#         if hasher.check_hashed_value(user_password, sql_data_password):
#             print(type(entries[0]))
#             return entries[0]
#         else:
#             return "INVALID LOG-IN"
#     except (Exception) as error:
#        return error
#     finally:
#         if connection is not None:
#             connection.close()


# def delete_user(user_email):
#     '''This allows us to delete a user'''
#     conn = establish_connection()
#     cur = conn.cursor()
#     user_delete_query = "DELETE FROM users WHERE email = %s"
#     try:
#         cur.execute(user_delete_query, (user_email,))
#         conn.commit()
#         return "Success"
#     except (Exception) as error:
#         return error
#     finally:
#         if conn is not None:
#             conn.close()


# def update_user(user_email, new_phonenumber):
#     '''This allows us to update the users phonenumber'''
#     conn = establish_connection()
#     cur = conn.cursor()
#     user_delete_query = "UPDATE users SET phonenumber = %s WHERE email = %s"
#     try:
#         cur.execute(user_delete_query, (new_phonenumber, user_email))
#         conn.commit()
#         return (
#             "Successfully updated user "
#             + user_email
#             + " phonenumber to "
#             + new_phonenumber
#         )
#     except (Exception) as error:
#         print("ERROR IN deleting", error)
#     finally:
#         if conn is not None:
#             conn.close()


# def get_user_by_id(user_id):
#     '''This allows us to get the user by their id'''
#     conn = establish_connection()
#     cur = conn.cursor()
#     user_delete_query = "SELECT * FROM users WHERE user_id = %s"
#     try:
#         cur.execute(user_delete_query, (user_id,))
#         user = cur.fetchall()
#         return user
#     except (Exception) as error:
#         print("ERROR IN selecting", error)
#     finally:
#         if conn is not None:
#             conn.close()


