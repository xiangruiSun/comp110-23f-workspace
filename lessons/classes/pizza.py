"""Defining a Class!"""

from __future__ import annotations
#so we can return Pizza
"""defining the underlying structure every instance of this class will have."""
#name of class equivalent to a type

class Pizza:

    #attributes
    #think of these as the variables each instance of my class will have
    #<name> : <type>
    size:str
    toppings: int
    gluten_free: bool
    #<attribute name>: <type>

    def __init__(self, inp_size: str, inp_top: int, inp_gf: bool): #pizza as its own argument.
        """My constructor."""
        #default name __init__
        #no specify return type
        #returns a Pizza object, no need to say returns
        #to access attribute value use <name>.<attribute name>
        self.size = inp_size
        self.toppings = inp_top
        self.gluten_free = inp_gf
    
    def price(self) -> float:
        """Calculate price of pizza."""
        if self.size == "large":
            price: float = 6.25
        else:
            price: float = 5.00
        price += .75 * self.toppings
        if self.gluten_free:
            price += 1.00
        return price
    
    def add_toppings(self, num_toppings: int):
        """Add toppings to existing pizza."""
        self.toppings += num_toppings
    
    def make_new_pizza_add_toppings(self, num_toppings: int) -> Pizza:
        """Make a new pizza with existing pizza's properties and add toppings"""
        new_pizza: Pizza = Pizza(self.size, self.toppings + num_toppings, self.gluten_free)
        return new_pizza
    
    def __str__(self) -> str:
        """Make print() to print the things we want."""
        pizza_info: str = f"PIZZA ORDER: size: {self.size}, toppings: {self.toppings}, GF: {self.gluten_free}"
        return pizza_info

my_pizza: Pizza = Pizza("medium", 2, False)
print(my_pizza) #print the memory location not itself

