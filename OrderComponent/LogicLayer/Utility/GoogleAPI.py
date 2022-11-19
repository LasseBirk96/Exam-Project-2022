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
        
    def __get_time(self, users_address, resturant_address):
        data = self.client.distance_matrix(users_address, resturant_address)
        rows = data.get("rows")
        elements = rows[0].get("elements")
        duration = elements[0].get("duration")
        time = duration.get("text")
        return time

    def get_delivery_information(self, users_address, resturant_address):
        distance = self.__get_distance(users_address, resturant_address)
        time = self.__get_time(users_address, resturant_address)
        return {"distance":distance, "time":time }