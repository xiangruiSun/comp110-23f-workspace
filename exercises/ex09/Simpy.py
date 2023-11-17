"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730525294"


class Simpy:
    """Defining a Simpy."""
    values: list[float]

    def __init__(self, list1: list[float]) -> None:
        """This is a constructor function for Simpy with list1 as the parameter."""
        self.values = list1
    
    def __str__(self) -> str:
        """This makes the print function print out the expected output."""
        info: str = ""
        info = f"Simpy({self.values})"
        return info

    def fill(self, float1: float, int1: int) -> None:
        """Fill in Simpy with float1 with int1 times."""
        self.values = []
        for elem in range(0, int1):
            self.values.append(float1)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in the values attribute with range of values."""
        assert step != 0.0
        value: float = start
        while (step > 0 and value < stop) or (step < 0 and value > stop):
            self.values.append(value)
            value += step

    def sum(self) -> float:
        """Sum all items in the values attribute."""
        summation: float = 0.0
        for elem in self.values:
            summation += elem
        return summation
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Use the addition operator in conjunction with Simpy objects and floats."""
        new_return: Simpy = Simpy([])
        if type(rhs) is float:
            for elem in self.values:
                new_return.values.append(elem + rhs)
            return new_return
        
        assert len(self.values) == len(rhs.values)
        id: int = 0
        while id < len(self.values):
            new_return.values.append(self.values[id] + rhs.values[id])
            id += 1
        return new_return
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Use the power operator in conjunction with Simpy objects and floats."""
        new_return: Simpy = Simpy([])
        if type(rhs) is float:
            for elem in self.values:
                new_return.values.append(elem ** rhs)
            return new_return
        
        assert len(self.values) == len(rhs.values)
        id: int = 0
        while id < len(self.values):
            new_return.values.append(self.values[id] ** rhs.values[id])
            id += 1
        return new_return
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """It has the ability to produce a mask, based on the equality of each item in Simpy object or float."""
        new_return: list[bool] = []
        if type(rhs) is float:
            for elem in self.values:
                if elem == rhs:
                    new_return.append(True)
                else:
                    new_return.append(False)
            return new_return
        
        assert len(self.values) == len(rhs.values)
        id: int = 0
        while id < len(self.values):
            if self.values[id] == rhs.values[id]:
                new_return.append(True)
            else:
                new_return.append(False)
            id += 1
        return new_return
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """It has the ability to produce a mask based on the greater than relationship between each item with Simpy or float."""
        new_return: list[bool] = []
        if type(rhs) is float:
            for elem in self.values:
                if elem > rhs:
                    new_return.append(True)
                else:
                    new_return.append(False)
            return new_return
        
        assert len(self.values) == len(rhs.values)
        id: int = 0
        while id < len(self.values):
            if self.values[id] > rhs.values[id]:
                new_return.append(True)
            else:
                new_return.append(False)
            id += 1
        return new_return
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Add the ability to use the subscription operator with Simpy objects."""
        if type(rhs) is int:
            new_return: float = 0.0
            new_return = self.values[rhs]
            return new_return
        else:
            New_Simpy: Simpy = Simpy([])
            id: int = 0
            while id < len(self.values):
                if rhs[id] is True:
                    New_Simpy.values.append(self.values[id])
                id += 1
            return New_Simpy