from DatabaseLayer.Queries import driver_mg_queries
from datetime import datetime, timedelta
import re
class PointCalculator:

    def __init__(self):
        pass


    def __get_time_of_order(self, order_id):

        #Get the order from mongo
        order = driver_mg_queries.get_order(order_id)

        #Get the time the order was placed
        time_of_order = order.get("time_ordered")

        # Get the time it should take to make the order
        delivery_info = order.get("delivery_information")
        expected_delivery_time_in_minutes = delivery_info.get("time")
    
        #Get the time it when the order should be delivered at the latest
        a = re.sub("[^0-9]", "", expected_delivery_time_in_minutes)
        expected_time_to_deliver = time_of_order + timedelta(minutes=int(a))

        return expected_time_to_deliver


    def calculate_points(self, order_id):
        expected_time_of_delivery = self.__get_time_of_order(order_id)
        actual_time_of_delivery = datetime.now()
        delta = (expected_time_of_delivery - actual_time_of_delivery)
        points = delta.total_seconds()
        if points < 0:
            points = 0
            return points
        return int(points)


