"""THIS CLASS DOES THINGS WITH OUR POSTGRES"""
import sys

sys.path.append("..")
from ..Connection.connector import establish_connection


def set_up_table(command):
    """This methods allows us to execute on or more quieres.
    However, in our case it is only used to set up one table"""
    connnection = establish_connection()
    cursor = connnection.cursor()
    try:
        cursor.execute(command)
        cursor.close()
        connnection.commit()
        print("Successfully created user table")
    except (Exception) as error:
        print(error)
    finally:
        if connnection is not None:
            connnection.close()


def return_products_table():
    """This method returns the SQL for creating a table called products"""
    return """
    CREATE TABLE IF NOT EXISTS products (
	    id SERIAL PRIMARY KEY,
        product_name VARCHAR(255) not NULL,
        product_description VARCHAR(255) not NULL,
        ingredients text[] not NULL,
        price SMALLINT not NULL
    );
    """



def set_up_products_table():
    set_up_table(return_products_table())