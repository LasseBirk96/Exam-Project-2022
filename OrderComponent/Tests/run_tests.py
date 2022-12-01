from .test_order_queries import test_insert_order
from OrderLogger.logger_creator import create_logger as log
def run():
    if all(
        [
            test_insert_order()

        ]
    ):
        log().info("ALL TESTS PASSED - STARTING SERVER")
        return True
    log().error("NOT ALL TESTS PASSED - NOT STARTING SERVER")
    return False

