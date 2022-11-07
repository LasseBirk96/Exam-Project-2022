"""THIS CLASS DOES THINGS WITH OUR POSTGRES"""
import sys

sys.path.append("..")
from Connection.connector import establish_connection


def set_up_table(command):
    """This methods allows us to execute on or more quieres.
    However, in our case it is only used to set up one table"""
    connnection = establish_connection()
    cursor = connnection.cursor()
    try:
        cursor.execute(command)
        cursor.close()
        connnection.commit()
        print("Successfully created table")
    except (Exception) as error:
        print(error)
    finally:
        if connnection is not None:
            connnection.close()


def return_user_table():
    """This method returns the SQL for creating a table called users"""
    return """
    CREATE TABLE IF NOT EXISTS users (
	user_id VARCHAR(255) primary KEY,
        first_name VARCHAR(255) not NULL,
        last_name VARCHAR(255) not NULL,
        password VARCHAR(255) not NULL,
        age SMALLINT not NULL,
        email VARCHAR(255) unique not NULL,
        phonenumber VARCHAR(255) unique not NULL
    );
    """



def set_up_user_table():
    set_up_table(return_user_table())