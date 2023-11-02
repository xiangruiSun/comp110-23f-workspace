"""Instantiating A class."""
"""
In order worders, we're creating objects that belong to that class.
"""
from lessons.classes.pizza import Pizza

my_pizza: Pizza = Pizza("large", 10, True) #Pizza() termed constructor
#use function Pizza("large") that created in pizza.py

#accessing/seting attributes
#my_pizza.size = "medium" #update the values
#my_pizza.toppings = 10
#my_pizza.gluten_free = True

# print("my_pizza: ")
# print(my_pizza) #instant by default print the object location

# print("Pizza:")
# print(Pizza) #stored as class

print("Size Attribute:")
print(my_pizza.size)

print("Toppings:")
print(my_pizza.toppings)

sals_pizza: Pizza = Pizza("medium", 5, False)
print(sals_pizza.size)

def price(input_pizza: Pizza) -> float:
    """Calculate the price of Pizza."""
    if input_pizza.size == "large":
         price: float = 6.25
    else:
         price: float = 5.00
    price += .75 * input_pizza.toppings
    if input_pizza.gluten_free:
         price += 1.00
    return price

print(price(sals_pizza))

#calling price function
print(price(sals_pizza))

#calling price method
print(sals_pizza.price())

my_pizza.add_toppings(2)
print(my_pizza.toppings)
print(my_pizza.price())

my_other_pizza: Pizza = my_pizza.make_new_pizza_add_toppings(2)
print(my_other_pizza.toppings)
print(my_pizza.toppings)