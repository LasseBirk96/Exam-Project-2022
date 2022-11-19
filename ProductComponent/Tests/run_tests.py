from .test_product_queries import test_persist_product, test_delete_product, test_get_all_products
from ProductLogger.logger_creator import create_logger as log



def run():
    if all(
        [
            test_persist_product(),
            test_delete_product(),
            test_get_all_products()
        ]
    ):
        log().info("ALL TESTS PASSED - STARTING SERVER")
        return True
    log().error("NOT ALL TESTS PASSED - NOT STARTING SERVER")
    return False

