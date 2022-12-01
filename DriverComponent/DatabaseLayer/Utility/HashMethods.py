from flask_bcrypt import Bcrypt
from flask import Flask
app = Flask(__name__)
bcrypt = Bcrypt(app)

class HashMethods:

    def __init__(self):
        pass

    def hash_value(self, value):
        encoded_value = bytes(value, encoding="utf-8")
        hashed_value = bcrypt.generate_password_hash(encoded_value)
        decoded_hashed_value = hashed_value.decode("utf-8")
        return decoded_hashed_value

    def check_hashed_value(self, value, o_value):
        value_from_api = bytes(value, encoding="utf-8")
        value_from_database = bytes(o_value, encoding="utf-8")
        if bcrypt.check_password_hash(value_from_database, value_from_api ):
            return True

