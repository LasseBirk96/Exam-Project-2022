from DatabaseLayer.Queries.product_queries import (
persist_product, delete_product, get_products
)


def test_persist_product(postgresql):
    # Arrange
    cur = postgresql.cursor()
    cur.execute(
      """
    CREATE TABLE IF NOT EXISTS products (
	    id SERIAL PRIMARY KEY,
        product_name VARCHAR(255) not NULL,
        product_description VARCHAR(255) not NULL,
        ingredients text[] not NULL,
        price SMALLINT not NULL
    );
    """
    )

    # Act
    persist_product("Orange Juice", "Incredibly disgusting acid", ["Filth", "oranges"], "30", postgresql)
    cur.execute("SELECT * FROM products;")

    # Assert
    assert len(cur.fetchall()) == 1


def test_delete_product(postgresql):
    # Arrange
    cur = postgresql.cursor()
    cur.execute(
      """
    CREATE TABLE IF NOT EXISTS products (
	    id SERIAL PRIMARY KEY,
        product_name VARCHAR(255) not NULL,
        product_description VARCHAR(255) not NULL,
        ingredients text[] not NULL,
        price SMALLINT not NULL
    );
    """
    )
    persist_product("Orange Juice", "Incredibly disgusting acid", ["Filth", "oranges"], "30", postgresql)

    # Assert
    cur.execute("SELECT * FROM products;")
    assert len(cur.fetchall()) == 1

    # Act
    delete_product("Orange Juice", postgresql)

    # Assert
    cur.execute("SELECT * FROM products;")
    assert len(cur.fetchall()) == 0



def test_get_product(postgresql):
    # Arrange
    cur = postgresql.cursor()
    cur.execute(
      """
    CREATE TABLE IF NOT EXISTS products (
	    id SERIAL PRIMARY KEY,
        product_name VARCHAR(255) not NULL,
        product_description VARCHAR(255) not NULL,
        ingredients text[] not NULL,
        price SMALLINT not NULL
    );
    """
    )
    persist_product("Orange Juice", "Incredibly disgusting acid", ["Filth", "oranges"], "30", postgresql)
    persist_product("Orange Juice", "Incredibly disgusting acid", ["Filth", "oranges"], "30", postgresql)
    persist_product("Orange Juice", "Incredibly disgusting acid", ["Filth", "oranges"], "30", postgresql)

    # Act
    products = get_products(postgresql)

    # Assert
    assert len(products) == 3
