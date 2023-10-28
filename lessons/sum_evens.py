"""Practice suming over lists"""


def sum_even_in_list(input_list: list[int]) -> int:
    """Sum evens."""
    list_sum: int = 0
    for elem in input_list:
        if elem % 2 == 0:
            list_sum += elem
    return list_sum