'''THIS CLASS CONTAINS ALL METHODS THAT QUERY THE POSTGRES DATABASE'''
import uuid
from flask_bcrypt import Bcrypt
from flask import Flask
from LogicLayer.Entities.User import User
from ..Utility.HashMethods import HashMethods
app = Flask(__name__)
bcrypt = Bcrypt(app)


def persist_user(first_name, last_name, password, age, email, phone_number, connection):
    '''This method persists a user'''
    user_id = str(uuid.uuid4())
    hasher = HashMethods()
    hashed_password = hasher.hash_value(password)
    user = User(
        user_id, first_name, last_name, hashed_password, age, email, phone_number
    )
    persist_user_query = "INSERT INTO users (user_id, first_name, last_name, password, age, email, phonenumber) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    cursor = connection.cursor()
    # Execute the tuple with tables
    try:
        cursor.execute(persist_user_query, user.return_user())
        connection.commit()
        return user_id
    except (Exception) as error:
       return error



def user_login(user_email, user_password, connection):
    '''This method allows the user to log in'''

    cursor = connection.cursor()
    user_login_query = "SELECT user_id, password FROM users WHERE email = %s"
    try:
        cursor.execute(user_login_query, (user_email,))
        entries = cursor.fetchall()[0]
        sql_data_password = entries[1]
        hasher = HashMethods()
        if hasher.check_hashed_value(user_password, sql_data_password):
            
            return entries[0]
        else:
            return "INVALID LOG-IN"
    except (Exception) as error:
       return error



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


# # def update_user(user_email, new_phonenumber):
# #     '''This allows us to update the users phonenumber'''
# #     conn = establish_connection()
# #     cur = conn.cursor()
# #     user_delete_query = "UPDATE users SET phonenumber = %s WHERE email = %s"
# #     try:
# #         cur.execute(user_delete_query, (new_phonenumber, user_email))
# #         conn.commit()
# #         return (
# #             "Successfully updated user "
# #             + user_email
# #             + " phonenumber to "
# #             + new_phonenumber
# #         )
# #     except (Exception) as error:
# #         print("ERROR IN deleting", error)
# #     finally:
# #         if conn is not None:
# #             conn.close()


def get_user_by_id(user_id, connection):
    '''This allows us to get the user by their id'''
    
    cur = connection.cursor()
    user_delete_query = "SELECT * FROM users WHERE user_id = %s"
    try:
        cur.execute(user_delete_query, (user_id,))
        user = cur.fetchall()
        return user
    except (Exception) as error:
        print("ERROR IN selecting", error)


