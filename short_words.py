"""Return list of words that are shorter than 5 characters."""
 
__author__ = "730525294"


def short_words(list1: list[str]) -> list[str]:
    """Return list of words that are shorter than 5 characters."""
    list2: list[str] = []
    for elem in list1:
        if len(elem) < 5:
            list2.append(elem)
        else:
            print(f"{elem} is too long!")
    return list2