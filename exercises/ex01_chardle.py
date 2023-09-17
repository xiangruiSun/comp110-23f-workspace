"""EX01 - Chardle - A cute tep toward Wordle."""

__author__ = "730525294"

number_instance: int = 0
word_name: str = input("Enter a 5-character word: ")

if len(word_name) != 5:
    print("Error: Word must contain 5 characters")
    exit()
else:
    word_search: str = input("Enter a single character: ")
    if len(word_search) != 1:
        print("Error: Character must be a single character.")
        exit()
    else:
        print("Searching for " + word_search + " in " + word_name)

if word_search == word_name[0]:
    number_instance = number_instance + 1
    print(word_search + " found at index 0")

if word_search == word_name[1]:
    number_instance = number_instance + 1
    print(word_search + " found at index 1")

if word_search == word_name[2]:
    number_instance = number_instance + 1
    print(word_search + " found at index 2")

if word_search == word_name[3]:
    number_instance = number_instance + 1
    print(word_search + " found at index 3")

if word_search == word_name[4]:
    number_instance = number_instance + 1
    print(word_search + " found at index 4")

if number_instance == 0:
    print("No instances of " + word_search + " found in " + word_name)

if number_instance == 1:
    print(str(number_instance) + " instance of " + word_search + " found in " + word_name)

if number_instance != 1 and number_instance != 0:
    print(str(number_instance) + " instances of " + word_search + " found in " + word_name)