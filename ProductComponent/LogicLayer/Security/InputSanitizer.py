import re

class InputSanitizer:

    def __init__(self):
        pass

    def clean_text(self, text):
        regex = r"\b^[A-Za-z_]*\b"
        if re.match(regex, text):
            return True
        return False


    def clean_number(self, number):
        regex = r"\b[0-9]{1,3}\b"
        if re.match(regex, number):
            return True

        return False



    def clean_input(self, data):
        if all(
            [
                self.clean_text(data.get("product_name")),
                self.clean_text(data.get("description")),
                self.clean_number(data.get("price"))
                
            ]
        ):
            
            return True
        return False


