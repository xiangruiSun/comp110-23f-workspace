"""EX02 wordle."""

__author__ = "730525294"

word_secret: str = "python"
word_guess: str = input(f"What is your {len(word_secret)}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
word_index: int = 0
result: str = ""

while len(word_guess) != len(word_secret):
    word_alternative: str = input(f"That was not {len(word_secret)} letters! Try again: ")
    word_guess = word_alternative
if len(word_guess) == len(word_secret):
    while word_index < len(word_secret): 
        if word_guess[word_index] == word_secret[word_index]:
            result += GREEN_BOX
        else:
            number_yellow: int = 0
            yellow_exist: bool = False
            while yellow_exist is not True and number_yellow < len(word_secret):
                if word_guess[word_index] == word_secret[number_yellow]:
                    yellow_exist = True
                    result += YELLOW_BOX
                else:
                    number_yellow += 1
            if yellow_exist is False:
                result += WHITE_BOX
        word_index += 1
    print(f"{ result }")

    if word_guess == word_secret:
        print("Woo! You got it!")
    else:
        print("Not quite. Play again soon!")
