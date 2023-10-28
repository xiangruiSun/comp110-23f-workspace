"""Testing my summation function."""

from lessons.sum_evens import sum_even_in_list


def test_empty_sum() -> None:
    """Test summation of empty list."""
    assert sum_even_in_list([]) == 0


def test_list_length_1():
    """Testing on a list with one element."""
    test_list: list[int] = [2]
    assert sum_even_in_list(test_list) == 2


def test_list_positive():
    "Summing positive integers."
    test_list: list[int] = [1,2,3,4]
    assert sum_even_in_list(test_list) == 6


def test_list_negs_and_pos():
    "Summing positive and negative integers."
    test_list: list[int] = [1,-2,3,4]
    assert sum_even_in_list(test_list) == 2