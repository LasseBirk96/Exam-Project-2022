from LogicLayer.Security.InputSanitizer import InputSanitizer
from BankingLogger.logger_creator import create_logger as log
from .Alligner import Alligner

def test_clean_input():
    formatter = Alligner()
    print(formatter.format("STARTING TEST ON test_clean_input"))
    sanitizer = InputSanitizer()
    data = {
	"email":"test@gmail.com",
	"account_number":"123456789012",
	"CVV":"012",
	"pin_code":"1111",
	"balance":500
    }
    if sanitizer.clean_input(data):
        log().info("TEST CLEAN INPUT PASSED")
        print(formatter.format("ENDING TEST ON test_clean_input"))
        return True
    log().info("TEST CLEAN INPUT FAILED")
    print(formatter.format("ENDING TEST ON test_clean_input"))
    return False