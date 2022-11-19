from DatabaseLayer.Queries import product_queries
from DatabaseLayer.Connection import connector
from ProductLogger.logger_creator import create_logger as log
from .Alligner import Alligner

def test_persist_product():
    formatter = Alligner()
    print(formatter.format("STARTING TEST ON test_persist_product"))
    product_name = "aaa"
    product_queries.persist_product(product_name, "A great test product", ["Test", "the", "code"], "99")
    log().info("PERSISTED PRODUCT TO DATABASE")
    connection = connector.establish_connection()
    cursor = connection.cursor()
    sql_query = "SELECT * FROM products WHERE product_name = %s"
    try:
        cursor.execute(sql_query, (product_name,))
        returned_product = cursor.fetchone()
        if returned_product is not None:
            log().info("PRODUCT SUCCESFULLY SELECTED")
            log().info("PRODUCT SUCCESFULLY DELETED")
            product_queries.delete_product(product_name)
            log().info(("TEST PERSIST PRODUCT PASSED"))
            return True
    except (Exception) as error:
        log().error("TEST PERSIST PRODUCT FAILED: " + str(error))
    finally:
        print(formatter.format("ENDING TEST ON test_persist_product"))
        if connection is not None:
            connection.close()



def test_delete_product():
    formatter = Alligner()
    print(formatter.format("STARTING TEST ON test_delete_product"))
    product_name = "AAA"
    product_queries.persist_product(product_name, "test", ["test", "test", "test"], "11")
    log().info("PERSISTED PRODUCT TO DATABASE")
    connection = connector.establish_connection()
    cursor = connection.cursor()
    sql_query = "DELETE FROM products WHERE product_name = %s"
    query = "SELECT * FROM products WHERE product_name = %s"
    try:
        cursor.execute(sql_query, (product_name,))
        cursor.execute(query, (product_name,))
        returned_product = cursor.fetchone()
        if returned_product is None:
            log().info("PRODUCT SUCCESFULLY DELETED")
            log().info(("TEST DELETE PRODUCT PASSED"))
            return True
    except (Exception) as error:
        log().error("TEST DELETE PRODUCT FAILED: " + str(error))
    finally:
        print(formatter.format("ENDING TEST ON test_delete_product"))
        if connection is not None:
            connection.close()


def test_get_all_products():
    formatter = Alligner()
    print(formatter.format("STARTING TEST ON test_get_all_products"))
    products = product_queries.get_products()
    if products is not None:
        log().info("GOT ALL PRODUCTS")
        log().info("TEST GET ALL PRODUCTS PASSED")
        log().info("ENDING TEST ON test_get_all_products")
        return True
    log().error("TEST GET ALL PRODUCTS FAILED")
    return False
