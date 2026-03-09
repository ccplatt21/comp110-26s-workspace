"""EX04 - List utility functions assignment"""

__author__ = "730672284"


def all(int_list: list[int], x: int) -> bool:
    """a function that takes a list and int and checks if int matches all of list"""
    # need to first make sure the list isn't just 0
    if len(int_list) == 0:
        return False

    # okay now a for loop checking each item and if it matches our "x" integer
    for item in int_list:
        if item != x:
            return False

    return True  # a return outside the loop if all match


def max(input: list[int]) -> int:
    """returns the largest in the list"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")

    # need a variable for the highest value
    max_value: int = input[0]
    # run through a loop that looks at each item and if that item is >, that is new max value
    for item in input:
        if item > max_value:
            max_value = item
    # return the max value at the end of the loop
    return max_value


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Checks if two lists that are inputted are exactly equal"""
    # if the lists aren't equal length return False
    if len(list1) != len(list2):
        return False

    # loop through each list with a variable

    idx: int = 0

    # a loop to go through both lists while idx
    while idx < len(list1) and idx < len(list2):

        # an if statment to compare the different indices
        if list1[idx] != list2[idx]:
            return False
        # add 1 to the variable so we check each index and don't get an error
        idx += 1

    return True  # outside the loop if all prior conditions are met


def extend(list1: list[int], list2: list[int]) -> None:
    """Appends the second list onto the first list"""
    # we need to add every value from the second list onto the first -- loop and append
    for item in list2:
        list1.append(
            item
        )  # we append list one with the item that we loop through and grab from 2
