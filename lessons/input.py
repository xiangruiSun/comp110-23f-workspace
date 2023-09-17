"""Demonstrates asking the user for input"""

user_name: str = input("What is your name? ")
print("Hello, " + user_name + ", good morning!")
print("You are the best programmer ever, " + user_name) 
#input function input() must be a str
#if we want the input to be other type of data
#we use chr(), int()