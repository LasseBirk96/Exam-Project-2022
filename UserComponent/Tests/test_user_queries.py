from .Alligner import Alligner
from UserLogger.logger_creator import create_logger as log
from DataBaseLayer.Connection import connector
from DataBaseLayer.Queries import user_queries



def test_persist_user():
    '''TEST IF USERS GET PERSISTED CORRECTLY'''
    formatter = Alligner()
    print(formatter.format("STARTING TEST ON test_persist_user"))
    email = "test@gmail.com"
    user_queries.persist_user("first_test", "last_test", "superSecurePassword", "11", email, "12345678")
    select_sql_query = "SELECT email FROM users WHERE email = %s"
    connection = connector.establish_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(select_sql_query, (email,))
        returned_email = cursor.fetchone()
        if returned_email is not None:
            user_queries.delete_user(email)
            log().info(("TEST PERSIST USER PASSED"))
            return True
    except (Exception) as error:
        log().error("TEST PERSIST USER FAILED: " + str(error))
    finally:
        print(formatter.format("ENDING TEST ON test_persist_user"))
        if connection is not None:
            connection.close()

#THIS NEEDS TO BE FIXED, DOESNT WORK CURRENTLY
def test_user_login():
    '''TEST IF USER CAN LOG IN'''
    formatter = Alligner()
    print(formatter.format("STARTING TEST ON test_user_login"))
    email = "test@gmail.com"
    user_queries.persist_user("first_test", "last_test", "superSecur1ePassword", "11", email, "12345678")

    try:
        thing = user_queries.user_login(email, "superSecurePassword")
        print(thing)
        if thing is not "INVALID LOG-IN":
            user_queries.delete_user(email)
            log().info("TEST LOGIN PASSED")
            return True
    
    except (Exception) as error:
        log().error("TEST USER LOGIN FAILED: " + str(error))
    finally:
        print(formatter.format("ENDING TEST ON test_user_login"))


