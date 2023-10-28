def odd_and_even(list1: list[int]) -> list[int]:
    """The function returns a new list containing the elements of the input that are odd and have an even index."""
    list2: list[int] = []
    for elem in range(0,len(list1)):
        if elem % 2 == 0 and list1[elem] % 2 == 1:
            list2.append(list1[elem])
    return list2