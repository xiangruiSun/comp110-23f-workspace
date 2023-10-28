"""Test my zip function."""
 
__author__ = "730525294"

from lessons.zip import zip


def test_equal_length() -> None:
    """Testing whether the function works given two lists with equal length."""
    assert zip(["a", "b", "c"], [4, 5, 6])


def test_equal_length_1() -> None:
    """Testing whether the function works given two lists with equal length one more."""
    assert zip(["e", "f", "g", "h"], [1, 2, 3, 4])


def test_not_equal_length() -> None:
    """Testing whether the function works given two lists with not equal length."""
    assert zip(["a", "b"], [4, 5, 6])
