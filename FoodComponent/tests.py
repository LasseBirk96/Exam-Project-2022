from LogicLayer.Entities.DishObject.Dish import Dish



#THIS DOES NEED TO BE MOVED, BUT PYTHON IMPORTING IS SUPER TOXIC

def test_initializing_of_dish_object():
    try:
        s = Dish("Tikka Masala", "A lovely little thing", ["Curry"], 515)
        assert ("Tikka Masala", "A lovely little thing", ["Curry"], 55) == (s.name, s.description, s.ingredients, s.price)
    except AssertionError:
        print("ERROR IN 'test_initializing_of_dish_object'")



if __name__ == "__main__":
    test_initializing_of_dish_object()
     
    print("Checking whether all tests are passed or not")

#HUSK FACADER OG DTO