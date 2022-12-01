class Driver:
    def __init__(self, driver_id, first_name, last_name, age, email, password, phone_number, points):
        self.driver_id = driver_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.points = points

    def return_driver(self):
        return (
        self.driver_id,
        self.first_name,
        self.last_name,
        self.age,
        self.email,
        self.password,
        self.phone_number,
        self.points
        )