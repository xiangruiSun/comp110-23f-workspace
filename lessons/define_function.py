"""Example functions to learn definition and calling syntax"""

def my_max(numb1: int, numb2: int) -> int:
    """Returns the maximum value out of two numbers"""
    if numb1 >= numb2:
        return numb1
    else:
        return numb2
#after return you exit the function
#you don't go down any further

#print(num1)
#outside the definition, num1 is undefined
#thus we are not able to print it
max_number: int = my_max(1,10)
print(max_number)

other_max_number : int = my_max(11,3)
print(other_max_number)
"""
variable_name: <return type> = function_name(<argument list)
def function_name(<parameer list>) -> <return type>
signature line
"""