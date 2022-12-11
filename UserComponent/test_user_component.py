import sys

sys.path.append("..")
from DatabaseLayer.Queries.user_queries import (
persist_user, user_login, get_user_by_id
)


def test_persist_user(postgresql):
    # Arrange
    cur = postgresql.cursor()
    cur.execute(
      """
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
    )

    # Act
    persist_user("lasse", "Birk", "adf", "12", "test@gmail.com", "2323", postgresql)
    cur.execute("SELECT * FROM users;")

    # Assert
    assert len(cur.fetchall()) == 1


def test_user_login(postgresql):
    # Arrange
    cur = postgresql.cursor()
    cur.execute(
      """
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
    )
    persist_user("lasse", "Birk", "adf", "12", "test@gmail.com", "2323", postgresql)

    # Act
    user_id = user_login("test@gmail.com", "adf", postgresql)

    # Assert
    assert user_id is not None


def test_get_user_by_id(postgresql):
    # Arrange
    cur = postgresql.cursor()
    cur.execute(
      """
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
    )
    user_id = persist_user(
        "lasse", "Birk", "adf", "12", "test@gmail.com", "2323", postgresql
    )
    

    # Act
    user = get_user_by_id(user_id, postgresql)
    print(user)

    # Assert
    assert user is not None
