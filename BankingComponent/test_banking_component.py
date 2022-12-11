import sys

sys.path.append("..")

from DatabaseLayer.Queries.bank_account_queries import (
persist_bank_account, handle_payment
)


def test_persist_bank_account(postgresql):
    # Arrange
    cur = postgresql.cursor()
    cur.execute(
    """
    CREATE TABLE IF NOT EXISTS bank_account (
    email VARCHAR(255) primary key unique,
	account_number VARCHAR(255) not NULL,
    CVV VARCHAR(255) not NULL,
    pin_code VARCHAR(255) not NULL,
    balance SMALLINT not NULL
    );
    """
    )

    # Act
    persist_bank_account("test@gmail.com", "123123", "111", "1231", 500, postgresql)
    cur.execute("SELECT * FROM bank_account;")

    # Assert
    assert len(cur.fetchall()) == 1


def test_handle_payment(postgresql):
    # Arrange
    cur = postgresql.cursor()
    cur.execute(
    """
    CREATE TABLE IF NOT EXISTS bank_account (
    email VARCHAR(255) primary key unique,
	account_number VARCHAR(255) not NULL,
    CVV VARCHAR(255) not NULL,
    pin_code VARCHAR(255) not NULL,
    balance SMALLINT not NULL
    );
    """
    )
    test_email = "test@gmail.com"
    persist_bank_account(test_email, "123123", "111", "1231", 500, postgresql)


    # Act
    handle_payment(test_email, "123123", "111", "1231", 200, postgresql)
    balance = cur.execute("SELECT balance FROM bank_account WHERE email = %s", (test_email,))

    # Assert
    assert cur.fetchall()[0][0] == 300