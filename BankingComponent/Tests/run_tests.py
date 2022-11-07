from .test_bank_account_queries import test_handle_payment, test_persist_bank_account
from .test_clean_input import test_clean_input
from BankingLogger.logger_creator import create_logger as log



def run():
    if all(
        [
            test_persist_bank_account(),
            test_handle_payment(),
            test_clean_input()

        ]
    ):
        log().info("ALL TESTS PASSED - STARTING SERVER")
        return True
    log().error("NOT ALL TESTS PASSED - NOT STARTING SERVER")
    return False

