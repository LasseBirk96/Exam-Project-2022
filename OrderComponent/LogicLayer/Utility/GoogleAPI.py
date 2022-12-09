import googlemaps
from decouple import config

api_key = config("api_key")

class GoogleAPI:

    def __init__(self):
        self.key = api_key
        self.client = googlemaps.Client(self.key)

    def __get_distance(self, users_address, resturant_address):
        data = self.client.distance_matrix(users_address, resturant_address)
        rows = data.get("rows")
        elements = rows[0].get("elements")
        distance = elements[0].get("distance")
        km = distance.get("text")
        return km
        
    def __get_time_based_on_distance(self, users_address, resturant_address):
        data = self.client.distance_matrix(users_address, resturant_address)
        rows = data.get("rows")
        elements = rows[0].get("elements")
        duration = elements[0].get("duration")
        time_ = duration.get("text")
        time = [int(s) for s in time_.split() if s.isdigit()][0]
        return time

    def __get_time_based_on_products(self, products):
        amount_of_products = len(products)
        time = amount_of_products * 10
        return time

    def get_delivery_information(self, users_address, resturant_address, products):
        distance = self.__get_distance(users_address, resturant_address)
        time_as_number = self.__get_time_based_on_distance(users_address, resturant_address) + self.__get_time_based_on_products(products)
        time_as_string = str(time_as_number) + "minutes"
        return {"distance":distance, "time":time_as_string }





