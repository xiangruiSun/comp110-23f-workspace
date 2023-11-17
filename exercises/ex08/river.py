"""File to define River class."""

__author__ = "730525294"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """Defining a river."""
    day: int
    bears: list[Bear]
    fish: list[Fish]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Check whether animals should be removed according to their age."""
        new_fish: list[Fish] = []
        new_bears: list[Bear] = []

        for elem in self.fish:
            if elem.age <= 3:
                new_fish.append(elem)

        for elem in self.bears:
            if elem.age <= 5:
                new_bears.append(elem)

        self.fish = new_fish
        self.bears = new_bears

        return None

    def bears_eating(self):
        """Modelling how each bear eats fish."""
        for elem in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                elem.eat(3)
        return None
    
    def check_hunger(self):
        """Remove bears when their hunger_score < 0."""
        new_bears: list[Bear] = []
        for elem in self.bears:
            if elem.hunger_score >= 0:
                new_bears.append(elem)
        self.bears = new_bears
        return None
        
    def repopulate_fish(self):
        """Each pair of fish will produce 4 offspring."""
        for x in range(0, (len(self.fish) // 2) * 4):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Each pair of Bear's will produce 1 offspring."""
        for x in range(0, len(self.bears) // 2):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """It prints out the fish, bear and day of the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Run river_day seven times."""
        for elem in range(0, 7):
            self.one_river_day()
        return None

    def remove_fish(self, amount: int):
        """Remove a desirable amount of fish."""
        for elem in range(0, amount):
            self.fish.pop(elem)