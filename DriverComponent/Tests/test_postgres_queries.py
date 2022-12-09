import sys

sys.path.append("..")
from DatabaseLayer.Queries.driver_pg_queries import persist_driver, driver_login, get_driver_by_id, get_points_by_id, update_driver_points


def test_persist_driver(postgresql):
    # Arrange    
    cur = postgresql.cursor() 
    cur.execute(
        """CREATE TABLE IF NOT EXISTS drivers (
	    driver_id VARCHAR(255) primary KEY,
        first_name VARCHAR(255) not NULL,
        last_name VARCHAR(255) not NULL,
        age SMALLINT not NULL,
        phonenumber VARCHAR(255) unique not NULL,
        email VARCHAR(255) unique not NULL,
        password VARCHAR(255) not NULL,
        points INTEGER not NULL
    );""")

    # Act
    persist_driver("lasse", "Birk", "adf", "12", "test@gmail.com", "2323", postgresql)
    cur.execute('SELECT * FROM drivers;') 

    # Assert
    assert len(cur.fetchall()) == 1   
   

def test_driver_login(postgresql):    
    # Arrange
    cur = postgresql.cursor()    
    cur.execute(
        """CREATE TABLE IF NOT EXISTS drivers (
	    driver_id VARCHAR(255) primary KEY,
        first_name VARCHAR(255) not NULL,
        last_name VARCHAR(255) not NULL,
        age SMALLINT not NULL,
        phonenumber VARCHAR(255) unique not NULL,
        email VARCHAR(255) unique not NULL,
        password VARCHAR(255) not NULL,
        points INTEGER not NULL
    );""")
    persist_driver("lasse", "Birk", "adf", "12", "test@gmail.com", "2323", postgresql)


    # Act 
    driver_id = driver_login("test@gmail.com", "adf", postgresql)

    # Assert
    assert driver_id is not None


    cur.execute('SELECT * FROM drivers;') 
    assert len(cur.fetchall()) == 1


def test_get_driver_by_id(postgresql):
    # Arrange
    cur = postgresql.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS drivers (
	    driver_id VARCHAR(255) primary KEY,
        first_name VARCHAR(255) not NULL,
        last_name VARCHAR(255) not NULL,
        age SMALLINT not NULL,
        phonenumber VARCHAR(255) unique not NULL,
        email VARCHAR(255) unique not NULL,
        password VARCHAR(255) not NULL,
        points INTEGER not NULL
    );""")
    driver_id = persist_driver("lasse", "Birk", "adf", "12", "test@gmail.com", "2323", postgresql)


    # Act
    driver = get_driver_by_id(driver_id, postgresql)

    # Assert
    assert driver is not None


def test_get_points_by_id(postgresql):
    # Arrange
    cur = postgresql.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS drivers (
	    driver_id VARCHAR(255) primary KEY,
        first_name VARCHAR(255) not NULL,
        last_name VARCHAR(255) not NULL,
        age SMALLINT not NULL,
        phonenumber VARCHAR(255) unique not NULL,
        email VARCHAR(255) unique not NULL,
        password VARCHAR(255) not NULL,
        points INTEGER not NULL
    );""")
    driver_id = persist_driver("lasse", "Birk", "adf", "12", "test@gmail.com", "2323", postgresql)

    # Act
    points = get_points_by_id(driver_id, postgresql)

    # Assert
    assert points is not None
    


def test_update_driver_points(postgresql):
    # Arrange
    cur = postgresql.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS drivers (
	    driver_id VARCHAR(255) primary KEY,
        first_name VARCHAR(255) not NULL,
        last_name VARCHAR(255) not NULL,
        age SMALLINT not NULL,
        phonenumber VARCHAR(255) unique not NULL,
        email VARCHAR(255) unique not NULL,
        password VARCHAR(255) not NULL,
        points INTEGER not NULL
    );""")
    driver_id = persist_driver("lasse", "Birk", "adf", "12", "test@gmail.com", "2323", postgresql)
    current_points = 300
    points_to_be_added = 100

    # Act

    new_total = update_driver_points(driver_id, points_to_be_added, current_points, postgresql)

    # Assert
    assert new_total == 400