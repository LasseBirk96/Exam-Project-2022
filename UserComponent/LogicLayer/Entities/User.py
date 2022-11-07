class User:
    def __init__(self, user_id, first_name, last_name, age, email, password, phone_number):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.password = password
        self.phone_number = phone_number

    def return_user(self):
        return (
        self.user_id,
        self.first_name,
        self.last_name,
        self.age,
        self.email,
        self.password,
        self.phone_number
        )