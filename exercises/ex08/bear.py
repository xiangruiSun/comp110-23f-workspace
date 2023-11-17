"""File to define Bear class."""


class Bear:
    """Defining a bear."""
    age: int
    hunger_score: int

    def __init__(self, age: int = 0, hungerlevel: int = 0):
        """This is a constructor function for bear."""
        self.age = age
        self.hunger_score = hungerlevel
        return None
    
    def one_day(self):
        """The bear ages 1 more."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Update the bear's hunger_score so that it increases by num_fish."""
        self.hunger_score += num_fish
        return None