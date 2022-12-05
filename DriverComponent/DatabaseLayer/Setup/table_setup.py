"""THIS CLASS DOES THINGS WITH OUR POSTGRES"""
import sys

sys.path.append("..")
from ..Connection.connect_to_postgres import establish_connection


def set_up_table(command):
    """This methods allows us to execute on or more quieres.
    However, in our case it is only used to set up one table"""
    connnection = establish_connection()
    cursor = connnection.cursor()
    try:
        cursor.execute(command)
        cursor.close()
        connnection.commit()
        print("Successfully created driver table")
    except (Exception) as error:
        print(error)
    finally:
        if connnection is not None:
            connnection.close()


def return_driver_table():
    """This method returns the SQL for creating a table called drivers"""
    return """
    CREATE TABLE IF NOT EXISTS drivers (
	driver_id VARCHAR(255) primary KEY,
        first_name VARCHAR(255) not NULL,
        last_name VARCHAR(255) not NULL,
        age SMALLINT not NULL,
        phonenumber VARCHAR(255) unique not NULL,
        email VARCHAR(255) unique not NULL,
        password VARCHAR(255) not NULL,
        points INTEGER not NULL
    );
    """



def set_up_driver_table():
    set_up_table(return_driver_table())


