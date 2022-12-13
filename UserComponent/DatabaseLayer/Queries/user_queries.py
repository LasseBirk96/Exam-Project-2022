'''THIS CLASS CONTAINS ALL METHODS THAT QUERY THE POSTGRES DATABASE'''
from DatabaseLayer.Connection import connector
import uuid
from LogicLayer.Entities.User import User
from DatabaseLayer.Utility.HashMethods import HashMethods


def persist_user(first_name, last_name, password, age, email, phone_number, connection = None):

    '''This method persists a user'''
    if connection == None:
        connection = connector.establish_connection()
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


def user_login(user_email, user_password, connection = None):
    '''This method allows the user to log in'''
    if connection == None:
        connection = connector.establish_connection()

    cursor = connection.cursor()
    user_login_query = "SELECT user_id, password FROM users WHERE email = %s"
    try:
        cursor.execute(user_login_query, (user_email,))
        entries = cursor.fetchall()[0]
        sql_data_password = entries[1]
        hasher = HashMethods()
        if hasher.check_hashed_value(user_password, sql_data_password):
            return entries[0]
    except (Exception) as error:
       return error


def get_user_by_id(user_id, connection = None):
    '''This allows us to get the user by their id'''
    if connection == None:
        connection = connector.establish_connection()
    
    cur = connection.cursor()
    user_delete_query = "SELECT * FROM users WHERE user_id = %s"
    try:
        cur.execute(user_delete_query, (user_id,))
        user = cur.fetchall()
        return user
    except (Exception) as error:
        return error


