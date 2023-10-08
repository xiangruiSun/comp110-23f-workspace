"""Game that only complete when you guess the right number"""

__author__ = "730525294"

from random import randint
#import a build-in function: randint
secret: int = randint(1,10)
guess: int = int(input("Guess a number between 1 and 10: "))
number_of_trial: int = 2
tries_count: int = 0
while (guess != secret) and (tries_count < number_of_trial):
    print("Wrong!")
    if (guess < 1) or (guess > 10):
        print("That's not between 1 and 10!")
    if guess > secret:
        print("Your gues was too high")
    else:
        print("Your guess was too low!")
    tries_count +=1
    guess = int(input("Guess again: "))
#control+c can exit the program immediately
#before exiting the while loop, the program will not run this code
if guess == secret:
    print("You got it!")