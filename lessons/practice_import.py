"""Practice importing from other modules"""

from lessons import my_functions
#from package name(lessons) import module name(my_functions)
#when importing my_function, it runs all
if __name__ == "__main__":
    print("Howdy!")
print(my_functions.addition(1,2))

print(my_functions.my_variable)
#variable: model name, variable name

from lessons.my_functions import addition
print(addition(1,2))

#<package name>.<module name> import <function name>
#we are still running the whole module but we can only refer to addition function