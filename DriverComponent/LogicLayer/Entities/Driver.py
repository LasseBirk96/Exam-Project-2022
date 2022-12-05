class Driver:

    def __init__(self, driver_id, first_name, last_name, age, phonenumber, email,  password, points):
        self.driver_id = driver_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phonenumber = phonenumber
        self.email = email
        self.password = password
        self.points = points

    
    def return_driver(self):
         return (
        self.driver_id,
        self.first_name,
        self.last_name,
        self.age,
        self.phonenumber,
        self.email,
        self.password,
        self.points
        )


    