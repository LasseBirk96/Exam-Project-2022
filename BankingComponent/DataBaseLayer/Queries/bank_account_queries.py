import sys

sys.path.append("..")
from ..Utility.HashMethods import HashMethods
from ..Connection.connector import establish_connection
from BankingComponent.LogicLayer.Entities.BankAccount import BankAccount
from BankingComponent.BankingLogger.logger_creator import create_logger as log


def persist_bank_account(email, account_number, CVV, pin_code, balance):
    """This method persists a bank account"""
    hasher = HashMethods()
    hashed_account_number = hasher.hash_value(account_number)
    hashed_CVV = hasher.hash_value(CVV)
    hashed_pin_code = hasher.hash_value(pin_code)
    bank_account = BankAccount(
        email, hashed_account_number, hashed_CVV, hashed_pin_code, balance
    )
    sql_query = "INSERT INTO bank_account (email, account_number, CVV, pin_code, balance) VALUES (%s, %s, %s, %s, %s)"
    connection = establish_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(sql_query, bank_account.return_account())
        connection.commit()
        log().info("COMMITETED ACCOUNT " + email + " TO DATABASE")
        return "Your account has been made succesfully"
    except (Exception) as error:
        log().error("ERROR IN persist_bank_account: " + str(error))
    finally:
        if connection is not None:
            connection.close()


def handle_payment(email, account_number, CVV, pin_code, price):
    if validate_data(email, account_number, CVV, pin_code):
        current_balance = get_balance_from_account(email)
        if price > current_balance:
            return "Can't make payment, not enough money in the account"
        connection = establish_connection()
        cursor = connection.cursor()
        try:
            sql_query = "UPDATE bank_account SET balance = %s WHERE email = %s"
            new_balance = current_balance - price
            cursor.execute(sql_query, (new_balance, email))
            connection.commit()
            log().info("ACCOUNT: " + email + " SUCCESSFUL PAYMENT")
            return "Payment Complete!"
        except (Exception) as error:
            log().error("ERROR IN handle_payment: " + str(error))
        finally:
            if connection is not None:
                connection.close()


def get_balance_from_account(email):
    sql_query = "SELECT balance FROM bank_account WHERE email = %s"
    connection = establish_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(sql_query, (email,))
        returned_balance = cursor.fetchone()
        balance = returned_balance[0]
        log().info("GOT BALANCE FROM ACCOUNT: " + email)
        return balance
    except (Exception) as error:
        log().error("ERROR IN get_balance_from_account: " + str(error))
    finally:
        if connection is not None:
            connection.close()


def validate_data(email, account_number, CVV, pin_code):
    sql_query = (
        "SELECT account_number, CVV, pin_code FROM bank_account WHERE email = %s"
    )
    connection = establish_connection()
    cursor = connection.cursor()
    hasher = HashMethods()
    try:
        cursor.execute(sql_query, (email,))
        returned_data = cursor.fetchall()
        data = returned_data[0]
        account_number_from_db = data[0]
        CVV_from_db = data[1]
        pin_code_from_db = data[2]
        if all([
                hasher.check_hashed_value(account_number, account_number_from_db),
                hasher.check_hashed_value(CVV, CVV_from_db),
                hasher.check_hashed_value(pin_code, pin_code_from_db)
            ]):
                log().info("DATA VALIDATED ON ACCOUNT: " + email)
                return True
    except (Exception) as error:
        log().error("ERROR IN validate_data: " + str(error))
    finally:
        if connection is not None:
            connection.close()


def delete_account_on_email(email):
    sql_query = "DELETE FROM bank_account WHERE email = %s"
    connection = establish_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(sql_query, (email,))
        connection.commit()
        return log().info("DELETED ACCOUNT: " + email)
    except (Exception) as error:
        log().error("ERROR IN delete_user_on_email: " + str(error))
    finally:
        if connection is not None:
            connection.close()
