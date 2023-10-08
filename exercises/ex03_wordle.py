"""ex03 wordle."""

__author__ = "730525294"


def contains_char(secret: str, guess_chr: str) -> bool:
    """To detect whether a single character from chr1 is found at any index of the string in str1."""
    assert len(guess_chr) == 1
    word_index: int = 0
    while word_index < len(secret):
        if secret[word_index] == guess_chr:
            return True
        else:
            word_index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Returns a string of emoji after inputting a guess and a secret."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    result: str = ""

    while index < len(secret):
        if contains_char(secret, guess[index]) is True:
            if guess[index] == secret[index]:
                result += GREEN_BOX
            else:
                result += YELLOW_BOX
        if contains_char(secret, guess[index]) is not True:
            result += WHITE_BOX
        index += 1
    return result


def input_guess(len_secret: int) -> str:
    """Prompt the user for a guess word until the guess word has expected length."""
    guess = input(f"Enter a {len_secret} character word: ")
    while len_secret != len(guess):
        guess = input(f"That wasn't {len_secret} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    secret: str = "codes"
    win: bool = False
    while win is False and turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            win = True
        else:
            turn += 1
    if win is False and turn > 6:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
