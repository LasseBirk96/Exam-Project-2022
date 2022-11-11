from .test_user_queries import test_persist_user, test_user_login
from UserLogger.logger_creator import create_logger as log



def run():
    if all(
        [
            test_user_login(),
            test_persist_user()

        ]
    ):
        log().info("ALL TESTS PASSED - STARTING SERVER")
        return True
    log().error("NOT ALL TESTS PASSED - NOT STARTING SERVER")
    return False

