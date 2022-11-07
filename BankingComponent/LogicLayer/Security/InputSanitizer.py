import re
from BankingLogger.logger_creator import create_logger as log
class InputSanitizer:

    def __init__(self):
        pass

    def __clean_email(self, email):
        """Checks if the email is valid"""
        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        if re.match(regex, email):
            return True
        log().error("EMAIL IS INVALID: " + email)
        return False


    def __clean_account_number(self, account_number):
        regex = r"\b[0-9]{12}\b"
        if re.match(regex, account_number):
            return True
        log().error("ACCOUNT NUMBER IS INVALID: " + account_number)
        return False


    def __clean_CVV(self, cvv):
        regex = r"\b[0-9]{3}\b"
        if re.match(regex, cvv):
            return True
        log().error("CVV IS INVALID: " + cvv)
        return False


    def __clean_pin_code(self, pin_code):
        regex = r"\b[0-9]{4}\b"
        if re.match(regex, pin_code):
            return True
        log().error("PIN CODE IS INVALID: " + pin_code)
        return False


    def __clean_amount(self, amount):
        regex = r"\b^[0-9]*$\b"
        if re.match(regex, str(amount)):
            return True
        log().error("AMOUNT IS INVALID:" + amount)
        return False

    def __get_amount(self, data):
        '''In our case it always either price or balance, so to reuse clean_input, we get the correct key from this'''
        if data.get("balance") == None:
            return data.get("price")
        return data.get("balance")

    def clean_input(self, data):
        if all(
            [
                self.__clean_email(data.get("email")),
                self.__clean_account_number(data.get("account_number")),
                self.__clean_CVV(data.get("CVV")),
                self.__clean_pin_code(data.get("pin_code")),
                self.__clean_amount(self.__get_amount(data))
            ]
        ):
            
            return True
        log().error("INPUT IS NOT VALID")
        return False


