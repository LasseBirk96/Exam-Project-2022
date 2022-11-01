class Dish:

    
    def __init__(self, name, description, ingredients, price):
        self.name = name
        self.description = description
        self.ingredients = ingredients
        self.price = price

    def return_object_values(self):
        return self.name, self.description, self.ingredients, self.price
