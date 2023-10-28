"""Solve the chanllenge question."""

__author__ = "730525294"


def w_sum(vals: list[float]) -> float:
    """This is a function sum up using a while loop."""
    i: int = 0
    rv: float = 0
    while i < len(vals):
        rv += vals[i]
        i += 1
    return rv


def f_sum(vals: list[float]) -> float:
    """This is a function sum up using a for in loop."""
    rv: float = 0
    for i in vals:
        rv += i
    return rv


def f_range_sum(vals: list[float]) -> float:
    """This is a function sum up using a for in range(len(vals))."""
    rv: float = 0
    for i in range(0, len(vals)):
        rv += vals[i]
    return rv