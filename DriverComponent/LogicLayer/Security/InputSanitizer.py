import re
from UserLogger.logger_creator import create_logger as log
class InputSanitizer:

    def __init__(self):
        pass

    def __clean_email(self, email):
        if email == None:
            return True
        """Checks if the email is valid"""
        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        if re.match(regex, email):
            return True
        log().error("EMAIL IS INVALID: " + email)
        return False


    def __clean_name(self, name):
        if name == None:
            return True
        regex = r"\b^[A-Za-z]*\b"
        if re.match(regex, name):
            return True
        log().error("NAME IS INVALID: " + name)
        return False


    def __clean_age(self, age):
        if age == None:
            return True
        regex = r"\b[0-9]{1,3}\b"
        if re.match(regex, age):
            return True
        log().error("AGE IS INVALID: " + age)
        return False


    def __clean_phone_number(self, phone_number):
        if phone_number == None:
            return True
        regex = r"\b[0-9]{8}\b"
        if re.match(regex, phone_number):
            return True
        log().error("PHONE NUMBER IS INVALID: " + phone_number)
        return False



    def clean_input(self, data):
        if all(
            [
                self.__clean_email(data.get("email")),
                self.__clean_age(data.get("age")),
                self.__clean_name(data.get("first_name")),
                self.__clean_name(data.get("last_name")),
                self.__clean_phone_number(data.get("phone_number"))
            ]
        ):
            
            return True
        log().error("INPUT IS NOT VALID")
        return False


