import sys
sys.path.append("..")
from ..Connection.connector import establish_connection


def set_up_table(command):
    conn = establish_connection()
    cur = conn.cursor()
    try:
        cur.execute(command)
        cur.close()
        conn.commit()
        print("Successfully created bank account table")
    except (Exception) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# Returns the sql query that creates a bank_account table
def return_table():
    return  """
    CREATE TABLE IF NOT EXISTS bank_account (
    email VARCHAR(255) primary key unique,
	account_number VARCHAR(255) not NULL,
    CVV VARCHAR(255) not NULL,
    pin_code VARCHAR(255) not NULL,
    balance SMALLINT not NULL
    );
    """


def setup_bank_account_table():
    set_up_table(return_table())
