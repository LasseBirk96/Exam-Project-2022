from DatabaseLayer.Setup import table_setup
from DatabaseLayer.Queries import product_queries
def run_setup():

    #SETS UP THE TABLE
    table_setup.set_up_products_table()


    #Create some products


    product_queries.persist_product("Pepperoni Pizza", "Amazing pizza made from real italians sweaty eyebrows", ["Tomato", "Swine", "Flour", "Basil"], 79)
    product_queries.persist_product("Hawaii Pizza", "Pineapple trash pizza", ["Tomato", "Swine", "Flour", "Basil", "Pineapple"], 89)
    product_queries.persist_product("House Special", "Pizza with all the ingredients we have, good luck", ["Tomato", "Swine", "Flour", "Basil", "pineapple", "fish", "nuts", "lettuce", "death sticks"], 119)
    


