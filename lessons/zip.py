"""Combining two lists into a dictionary."""

__author__ = "730525294"


def zip(list1: list[str], list2: list[int]) -> dict[str, int]:
    """It combines two lists into a dictionary."""
    id: int = 0
    dictionary: dict[str, int] = {}
    if len(list1) == len(list2):
        while id < len(list1):
            dictionary[list1[id]] = list2[id]
            id += 1
        return dictionary
    return dictionary