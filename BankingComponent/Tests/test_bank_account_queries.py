from DataBaseLayer.Queries import bank_account_queries
from DataBaseLayer.Connection import connector
from BankingLogger.logger_creator import create_logger as log


def alligner(txt: str, width=100, filler='-', align='c'):
    assert align in 'lcr'
    return {'l': txt.ljust, 'c': txt.center, 'r': txt.rjust}[align](width, filler)



def test_persist_bank_account():
    '''TEST IF ACCOUNTS ARE PERSISTED CORRECTLY'''
    print(alligner("STARTING TEST ON test_persist_bank_account"))
    email = "test@gmail.com"
    bank_account_queries.persist_bank_account(email, "123456789012", "111", "1111", 500)
    select_sql_query = "SELECT email FROM bank_account WHERE email = %s"
    connection = connector.establish_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(select_sql_query, (email,))
        returned_email = cursor.fetchone()
        if returned_email is not None:
            bank_account_queries.delete_account_on_email(email)
            log().info(("TEST PERSIST BANK ACCOUNT PASSED"))
            return True
    except (Exception) as error:
        log().error("TEST PERSIST BANK ACCOUNT FAILED: " + str(error))
    finally:
        print(alligner("ENDING TEST ON test_persist_bank_account"))
        if connection is not None:
            connection.close()


def test_handle_payment():
    "TEST IF PAYMENT IS HANDLED CORRECTLY"
    print(alligner("STARTING TEST ON test_handle_payment"))
    email = "test@gmail.com"
    bank_account_queries.persist_bank_account(email, "123456789012", "111", "1111", 500)
    bank_account_queries.handle_payment(email, "123456789012", "111", "1111", 300)
    balance = bank_account_queries.get_balance_from_account(email)
    if balance == 200:
            bank_account_queries.delete_account_on_email(email)
            log().info("TEST HANDLE PAYMENT PASSED")
            print(alligner("ENDING TEST ON test_handle_payment"))
            return True
    bank_account_queries.delete_account_on_email(email)
    log().error("TEST HANDLE PAYMENT FAILED")
    print(alligner("ENDING TEST ON test_handle_payment"))
    return False



    
def run_tests():
    if test_persist_bank_account():
        if test_handle_payment():
            log().info("TESTS PASSED - STARTING SERVER")
            return True

    log().error("TESTS FAILED - NOT STARTING SERVER")
    return False
