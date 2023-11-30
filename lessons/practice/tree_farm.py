from __future__ import annotations

class ChristmasTreeFarm:
    """Defining a farm."""
    plots: list[int]

    def __init__(self, plots: int, initial_planting: int):
        """This is a constructor function."""
        self.plots = []
        for integer in range(0, initial_planting):
            self.plots.append(1)
        for integer1 in range(0, plots - initial_planting):
            self.plots.append(0)

    def plant(self, index: int) -> None:
        """Plant one baby tree at a specific index."""
        self.plots[index] = 1

    def growth(self) -> None:
        """Grow each plante tree by 1."""
        for id in range(0, len(self.plots)):
            if self.plots[id] != 0:
                self.plots[id] += 1
    
    def harvest(self, replant: bool) -> int:
        """Harvest trees and replant them."""
        id: int = 0
        count: int = 0
        for id in range(0, len(self.plots)):
            if self.plots[id] >= 5:
                count += 1
                if replant is True:
                    self.plots[id] = 1
                else: self.plots[id] = 0
        return count
    
    def __add__(self, other: ChristmasTreeFarm) -> ChristmasTreeFarm:
        """Add two ChristmasTreeFarm together."""
        count: int = 0
        for elem1 in self.plots:
            if elem1 != 0:
                count += 1
        for elem in other.plots:
            if elem != 0:
                count += 1
        New: ChristmasTreeFarm = ChristmasTreeFarm(len(self.plots + other.plots), count)
        return New