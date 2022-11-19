import re
from ProductLogger.logger_creator import create_logger as log

class InputSanitizer:

    def __init__(self):
        pass

    def __clean_text(self, text):
        regex = r"\b^[A-Za-z]*\b"
        if re.match(regex, text):
            return True
        log().error("INPUT IS INVALID: " + text)
        return False


    def __clean_number(self, number):
        regex = r"\b[0-9]{1,3}\b"
        if re.match(regex, number):
            return True
        log().error("INPUT IS INVALID: " + number)
        return False



    def clean_input(self, data):
        if all(
            [
                self.__clean_text(data.get("product_name")),
                self.__clean_text(data.get("description")),
                self.__clean_number(data.get("price"))
                
            ]
        ):
            
            return True
        log().error("INPUT IS NOT VALID")
        return False


