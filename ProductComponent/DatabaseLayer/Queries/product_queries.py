'''THIS CLASS CONTAINS ALL METHODS THAT QUERY THE POSTGRES DATABASE'''
from ..Connection.connector import establish_connection
from flask_bcrypt import Bcrypt
from flask import Flask, request, jsonify
from LogicLayer.Entities.Product import Product
app = Flask(__name__)
bcrypt = Bcrypt(app)


def persist_product(product_name, description, ingredients, price):
    '''This method persists a product'''
    product = Product(product_name, description, ingredients, price)
    persist_user_query = "INSERT INTO products (product_name, product_description, ingredients, price) VALUES (%s, %s, %s, %s)"
    connection = establish_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(persist_user_query, product.return_product())
        connection.commit()
        return "Success"
    except (Exception) as error:
        return error
    finally:
        if connection is not None:
            connection.close()


def delete_product(product_name):
    '''This allows us to delete a product'''
    connection = establish_connection()
    cursor = connection.cursor()
    product_delete_query = "DELETE FROM products WHERE product_name = %s"
    try:
        cursor.execute(product_delete_query, (product_name,))
        connection.commit()
        return product_name
    except (Exception) as error:
         return error
    finally:
        if connection is not None:
            connection.close()


#MAYBE MAKE THIS RETURN EVERYTHING AS DICTS IF NEEDED
def get_products():
    connection = establish_connection()
    cursor = connection.cursor()
    get_products_query = "SELECT * FROM products"
    try:
        cursor.execute(get_products_query)
        products = cursor.fetchall()
        return jsonify(products)
    except (Exception) as error:
        return error
    finally:
        if connection is not None:
            connection.close()
