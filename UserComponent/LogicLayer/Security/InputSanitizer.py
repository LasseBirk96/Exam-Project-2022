import re
class InputSanitizer:

    def __init__(self):
        pass

    def clean_email(self, email):
        if email == None:
            return True
        """Checks if the email is valid"""
        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        if re.match(regex, email):
            return True
        return False


    def clean_name(self, name):
        if name == None:
            return True
        regex = r"\b^[a-zA-Z]+$\b"
        if re.match(regex, name):
            return True
        return False


    def clean_age(self, age):
        if age == None:
            return True
        regex = r"\b[0-9]{1,3}\b"
        if re.match(regex, age):
            return True

        return False


    def clean_phonenumber(self, phone_number):
        if phone_number == None:
            return True
        regex = r"\b[0-9]{8}\b"
        if re.match(regex, phone_number):
            return True

        return False



    def clean_input(self, data):
        if all(
            [
                self.clean_email(data.get("email")),
                self.clean_age(data.get("age")),
                self.clean_name(data.get("first_name")),
                self.clean_name(data.get("last_name")),
                self.clean_phonenumber(data.get("phone_number"))
            ]
        ): 
            return True
        return False


