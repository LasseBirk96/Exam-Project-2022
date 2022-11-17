class Order:
    def __init__(self, email, phone, products, distance_to_address, delivery_time):
        self.email = email
        self.phone = phone
        self.products = products
        self.distance_to_address = distance_to_address
        self.delivery_time = delivery_time

    def return_order(self):
        return {
            "email": self.email,
            "phone": self.phone,
            "products": self.products,
            "distance_to_address": self.distance_to_address,
            "delivery_time": self.delivery_time
        }