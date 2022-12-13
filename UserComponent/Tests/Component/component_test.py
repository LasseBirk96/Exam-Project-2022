from LogicLayer.ComponentAPI.Handler import Handler


def test_handle_persist_user(postgresql):
    '''This test should return True, as the input is correct'''
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
    data = {
	"first_name":"Lasse",
	"last_name":"Birk",
	"password":"hejhej123",
	"age":"23",
	"email":"test1@gmail.com",
	"phone_number":"12345618"
    }


    # Act
    Handler.handle_persist_user(data, postgresql)
    cur.execute("SELECT * FROM users;")
    # Assert


    # Assert
    assert len(cur.fetchall()) == 1

def test_handle_persist_user_false_positive(postgresql):
    '''This test should return False, as the input is not correct'''
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
    data = {
	"first_name":"La31311313se",
	"last_name":"Bi123123rk",
	"password":"hejhej123",
	"age":"23111",
	"email":"test1>>>>>@gmail.com",
	"phone_number":"1234qqwqq5618"
    }


    # Act
    Handler.handle_persist_user(data, postgresql)
    cur.execute("SELECT * FROM users;")
    # Assert


    # Assert
    assert len(cur.fetchall()) == 0


def test_handle_user_login(postgresql):
    '''This test should return not None, as the input is correct'''
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
    data = {
	"first_name":"Lasse",
	"last_name":"Birk",
	"password":"hejhej123",
	"age":"23",
	"email":"test1@gmail.com",
	"phone_number":"12345618"
    }
    Handler.handle_persist_user(data, postgresql)
    login_data = {"email":"test1@gmail.com", "password":"hejhej123"}


    # Act

    response = Handler.handle_user_login(login_data, postgresql)

    # Assert
    assert response is not None




def test_handle_user_login_false_positive(postgresql):
    '''This test should return None, as the input is incorrect'''
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
    data = {
	"first_name":"Lasse",
	"last_name":"Birk",
	"password":"hejhej123",
	"age":"23",
	"email":"testqq1@gmail.com",
	"phone_number":"12345618"
    }
    Handler.handle_persist_user(data, postgresql)
    login_data = {"email":"test1@gmail.com", "password":"hejhej123"}


    # Act

    response = Handler.handle_user_login(login_data, postgresql)

    # Assert
    assert response is None
