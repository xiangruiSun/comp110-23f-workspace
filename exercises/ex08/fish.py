"""File to define Fish class."""


class Fish:
    """Defining a fish."""
    age: int

    def __init__(self, age_input: int = 0):
        """This is a constructor function for fish."""
        self.age = age_input
        return None
    
    def one_day(self):
        """Fish ages 1 more."""
        self.age += 1
        return None