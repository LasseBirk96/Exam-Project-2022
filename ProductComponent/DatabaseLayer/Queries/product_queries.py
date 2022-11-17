'''THIS CLASS CONTAINS ALL METHODS THAT QUERY THE POSTGRES DATABASE'''
import uuid
from ..Connection.connector import establish_connection
from flask_bcrypt import Bcrypt
from flask import Flask
from LogicLayer.Entities.Product import Product
from ProductLogger.logger_creator import create_logger as log
app = Flask(__name__)
bcrypt = Bcrypt(app)


def persist_product(product_name, description, ingredients, price):
    '''This method persists a product'''
    product = Product(product_name, description, ingredients, price)
    persist_user_query = "INSERT INTO products (product_name, product_description, ingredients, price) VALUES (%s, %s, %s, %s)"
    connection = establish_connection()
    cursor = connection.cursor()
    # Execute the tuple with tables
    try:
        cursor.execute(persist_user_query, product.return_product())
        connection.commit()
        log().info("COMMITTED PRODUCT " + product_name + " TO DATABASE")
        return "Your product has been made"
    except (Exception) as error:
        log().error("ERROR IN persist_product: " + str(error))
    finally:
        if connection is not None:
            connection.close()




# def delete_user(user_email):
#     '''This allows us to delete a user'''
#     conn = establish_connection()
#     cur = conn.cursor()
#     user_delete_query = "DELETE FROM users WHERE email = %s"
#     try:
#         cur.execute(user_delete_query, (user_email,))
#         conn.commit()
#         return "Successfully deleted user" + user_email
#     except (Exception) as error:
#         print("ERROR IN deleting", error)
#     finally:
#         if conn is not None:
#             conn.close()

