"""Construct list Uility Function."""

__author__ = "730525294"


def all(list_int: list[int], int_find: int) -> bool:
    """To detect whether all the ints in the list are the same as the given int."""
    idx: int = 0
    if list_int == []:
        return False
    
    while idx < len(list_int):
        if list_int[idx] != int_find:
            return False
        idx += 1
    return True


def max(list_int: list[int]) -> int:
    """To return the largest int in the list."""
    if len(list_int) == 0:
        raise ValueError("max() arg is an empty List")
    
    int_max: int = list_int[0]
    idx: int = 0

    while idx < len(list_int):
        if int_max < list_int[idx]:
            int_max = list_int[idx]
        idx += 1
    return int_max


def is_equal(list_1: list[int], list_2: list) -> bool:
    """To identify whether two lists are identical."""
    idx: int = 0
    if len(list_1) != len(list_2):
        return False
    
    while idx < len(list_1):
        if list_1[idx] == list_2[idx]:
            idx += 1
        else:
            return False
    return True       