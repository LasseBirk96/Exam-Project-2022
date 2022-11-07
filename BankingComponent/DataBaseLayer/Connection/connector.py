
'''THIS CLASS ENABLES US TO CONNECT TO OUR POSTGRES'''
import os
import time
from psycopg2 import connect, OperationalError
from BankingComponent.BankingLogger.logger_creator import create_logger as log

def establish_connection(tries = 3, timeout = 5):
    if tries == 0:
        log().info("Could not connect after multiple tries")
        raise Exception("Could not connect after multiple tries")

    try:
        return connect(
            dbname = os.environ.get('POSTGRES_DB'),
            user = os.environ.get('POSTGRES_USER'),
            password = os.environ.get('POSTGRES_PASSWORD'),
            host = os.environ.get('POSTGRES_HOST'),
            port = os.environ.get('POSTGRES_PORT')
        )
    except OperationalError:
        log().info((f"Could not connect. Retrying in {timeout} seconds"))
        time.sleep(timeout)
        return establish_connection(tries-1, timeout)


