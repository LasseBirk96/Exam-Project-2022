import sys

sys.path.append("..")
from ..Utility.HashMethods import HashMethods
from ..Connection import connector
from LogicLayer.Entities.BankAccount import BankAccount
from BankingLogger.logger_creator import create_logger as log


def persist_bank_account(email, account_number, CVV, pin_code, balance, connection = None):
    """This method persists a bank account"""
    if connection == None:
        connection = connector.establish_connection()
    hasher = HashMethods()
    hashed_account_number = hasher.hash_value(account_number)
    hashed_CVV = hasher.hash_value(CVV)
    hashed_pin_code = hasher.hash_value(pin_code)
    bank_account = BankAccount(
        email, hashed_account_number, hashed_CVV, hashed_pin_code, balance
    )
    sql_query = "INSERT INTO bank_account (email, account_number, CVV, pin_code, balance) VALUES (%s, %s, %s, %s, %s)"
    cursor = connection.cursor()
    try:
        cursor.execute(sql_query, bank_account.return_account())
        connection.commit()
        return "Success"
    except (Exception) as error:
        return error


def handle_payment(email, account_number, CVV, pin_code, price, connection = None):
    if connection == None:
        connection = connector.establish_connection()
    if validate_data(email, account_number, CVV, pin_code, connection):
        current_balance = get_balance_from_account(email, connection)
        if price > current_balance:
            return "Can't make payment, not enough money in the account"
        cursor = connection.cursor()
        try:
            sql_query = "UPDATE bank_account SET balance = %s WHERE email = %s"
            new_balance = current_balance - price
            cursor.execute(sql_query, (new_balance, email))
            connection.commit()
            return "Success"
        except (Exception) as error:
            return error


def get_balance_from_account(email, connection = None):
    if connection == None:
        connection = connector.establish_connection()
    sql_query = "SELECT balance FROM bank_account WHERE email = %s"
    cursor = connection.cursor()
    try:
        cursor.execute(sql_query, (email,))
        returned_balance = cursor.fetchone()
        balance = returned_balance[0]
        return balance
    except (Exception) as error:
        return error


def validate_data(email, account_number, CVV, pin_code, connection = None):
    if connection == None:
        connection = connector.establish_connection()
    sql_query = (
        "SELECT account_number, CVV, pin_code FROM bank_account WHERE email = %s"
    )
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
                return True
    except (Exception) as error:
        return error



def delete_account_on_email(email, connection = None):
    if connection == None:
        connection = connector.establish_connection()
    sql_query = "DELETE FROM bank_account WHERE email = %s"
    cursor = connection.cursor()
    try:
        cursor.execute(sql_query, (email,))
        connection.commit()
    except (Exception) as error:
        return error
