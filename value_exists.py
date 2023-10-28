def value_exists(dict1: dict[str,int], int1: int) -> bool:
    """It returns True if int is in dict and returns false if otherwise."""
    for elem in dict1:
        if dict1[elem] == int1:
            return True
    return False