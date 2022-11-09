'''THIS CLASS CONTAINS ALL METHODS THAT QUERY THE POSTGRES DATABASE'''
import uuid
import sys


from ..Connection.connector import establish_connection
from flask_bcrypt import Bcrypt
from flask import Flask
from LogicLayer.Entities.User import User
from ..Utility.HashMethods import HashMethods
from UserLogger.logger_creator import create_logger as log
app = Flask(__name__)
bcrypt = Bcrypt(app)


def persist_user(first_name, last_name, password, age, email, phone_number):
    '''This method persists a user'''
    user_id = str(uuid.uuid4())
    hasher = HashMethods()
    hashed_password = hasher.hash_value(password)
    user = User(
        user_id, first_name, last_name, hashed_password, age, email, phone_number
    )
    persist_user_query = "INSERT INTO users (user_id, first_name, last_name, password, age, email, phonenumber) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    connection = establish_connection()
    cursor = connection.cursor()
    # Execute the tuple with tables
    try:
        cursor.execute(persist_user_query, user.return_user())
        connection.commit()
        log().info("COMMITTED USER " + email + " TO DATABASE")
        return "Your account has been made succesfully"
    except (Exception) as error:
        log().error("ERROR IN persist_user: " + str(error))
    finally:
        if connection is not None:
            connection.close()


def user_login(user_email, user_password):
    '''This method allows the user to log in'''
    connection = establish_connection()
    cursor = connection.cursor()
    user_login_query = "SELECT user_id, password FROM users WHERE email = %s"
    try:
        cursor.execute(user_login_query, (user_email,))
        entries = cursor.fetchall()[0]
        sql_data_password = entries[1]
        hasher = HashMethods()
        if hasher.check_hashed_value(user_password, sql_data_password):
            log().info("USER LOGGED IN SUCCESFULLY")
            return entries[0]
        else:
            log().error("INVALID LOG-IN")
            return "INVALID LOG-IN"
    except (Exception) as error:
       log().error("ERROR IN user_login" + str(error))
    finally:
        if connection is not None:
            connection.close()


def delete_user(user_email):
    '''This allows us to delete a user'''
    conn = establish_connection()
    cur = conn.cursor()
    user_delete_query = "DELETE FROM users WHERE email = %s"
    try:
        cur.execute(user_delete_query, (user_email,))
        conn.commit()
        return "Successfully deleted user" + user_email
    except (Exception) as error:
        print("ERROR IN deleting", error)
    finally:
        if conn is not None:
            conn.close()


def update_user(user_email, new_phonenumber):
    '''This allows us to update the users phonenumber'''
    conn = establish_connection()
    cur = conn.cursor()
    user_delete_query = "UPDATE users SET phonenumber = %s WHERE email = %s"
    try:
        cur.execute(user_delete_query, (new_phonenumber, user_email))
        conn.commit()
        return (
            "Successfully updated user "
            + user_email
            + " phonenumber to "
            + new_phonenumber
        )
    except (Exception) as error:
        print("ERROR IN deleting", error)
    finally:
        if conn is not None:
            conn.close()


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


# def get_user(user_email):
#     '''This allows us to get the user by their email'''
#     conn = establish_connection()
#     cur = conn.cursor()
#     user_delete_query = "SELECT * FROM users WHERE email = %s"
#     try:
#         cur.execute(user_delete_query, (user_email,))
#         user = cur.fetchall()
#         return user
#     except (Exception) as error:
#         print("ERROR IN selecting", error)
#     finally:
#         if conn is not None:
#             conn.close()