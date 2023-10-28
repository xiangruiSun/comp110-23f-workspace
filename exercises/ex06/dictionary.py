"""Doing dictionary exercise."""

__author__ = "730525294"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Invert the key and value in a dictionary."""
    count: dict[str, int] = {}
    for values in dict1.values():
        count[values] = 0
    
    for values1 in dict1.values():
        count[values1] += 1
    
    for number in count.values():
        if number > 1:
            raise KeyError()

    dict2: dict[str, str] = {}
    for key in dict1:
        value: str = dict1[key]
        dict2[value] = key
    return dict2


def favorite_color(dict1: dict[str, str]) -> str:
    """The function returns the color that appears most frequently."""
    count: dict[str, int] = {}
    for values in dict1.values():
        count[values] = 0
    
    for values1 in dict1.values():
        count[values1] += 1

    max_color: str = ""
    max_number: int = 0

    for key in count:
        if count[key] > max_number:
            max_number = count[key]
            max_color = key
    return max_color


def count(list1: list[str]) -> dict[str, int]:
    """It counts the number of unique values appearing in list1."""
    dict1: dict[str, int] = {}
    for elem in list1:
        if elem in dict1:
            dict1[elem] += 1
        else:
            dict1[elem] = 1
    return dict1


def alphabetizer(list1: list[str]) -> dict[str, list[str]]:
    """It produces a dictionary that categorizes element in list one according to its first letter."""
    dict1: dict[str, list[str]] = {}
    for elem in list1:
        if elem[0] not in dict1:
            dict1[elem[0].lower()] = [elem]
        else:
            dict1[elem[0].lower()].append(elem)
    return dict1


def update_attendance(dict1: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """It produces a dict to update attendance."""
    if day in dict1:
        dict1[day].append(student)
    else:
        dict1[day] = [student]
    return dict1