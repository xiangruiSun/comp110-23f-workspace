"""Practicing while loop in function"""

def mimic(my_words: str) -> str:
    """Given the string my_word, outputs the same stringß"""
    return my_words

mimic("abc")
#calling the function

def mimic(my_words: str, letter_idx: int) -> str:
    """Outputs the character of my_words at index letter_idx"""
    if letter_idx < len(my_words):
        return my_words[letter_idx]
    return "Too high of an index"

my_word: str = input("input a word: ")
index: int = int(input("Input an integer: "))
print(mimic(my_word,index))    

