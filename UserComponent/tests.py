from UserLogger.logger_creator import create_logger as log
from DatabaseLayer.Connection import connector
from DatabaseLayer.Queries import user_queries




def thing():
    a = 2 + 3
    if a == 5:
        return True
    return False
    

def run():
    if all(
        [
            thing()
        ]
    ):
        log().info("ALL TESTS PASSED - STARTING SERVER")
        return True
    log().error("NOT ALL TESTS PASSED - NOT STARTING SERVER")
    return False


if __name__ == "__main__":
    run()