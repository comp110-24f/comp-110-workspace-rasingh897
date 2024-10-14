"""Practicing reverse engineering and abstractions."""

__author__ = "730809199"


def all(list: list[int], num: int) -> bool:
    """returns True or False if all numbers in the list match the given integer"""
    if len(list) == 0:
        return False
    for nums in list:
        if num != nums:
            return False
    return True


# the return false can be in the for loop but if it never returns false after iterating
# through every value in the last it will exit the for loop and return True


def max(input: list[int]) -> int:
    """Returns the max int in a list"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    the_max: int = input[0]
    # making this local variable adds a place holder to add the max value to
    idx: int = 0
    while idx < len(input):
        if input[idx] > the_max:
            the_max = input[idx]
        idx += 1
        # the increase value for the index has to be outside the if section but within
        # the while loop
    return the_max


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Returns true or false whether the two lists of int values are equal at every index."""
    idx: int = 0
    result: bool = False
    if len(list_1) == 0 and len(list_2) == 0:
        return True
    if len(list_1) == len(list_2):
        while idx < len(list_1):
            if list_1[idx] == list_2[idx]:
                result = True
            else:
                result = False
                # orginially I did not add th extra else statement, but without it the
                # value of result will remain True because there would be no place for it
                # to change
            idx += 1
    return result


def extend(input_1: list[int], input_2: list[int]) -> None:
    idx: int = 0
    while idx < len(input_2):
        input_1.append(input_2[idx])
        idx += 1


# while iterating through the index, each value at that index of the second list will be
# added to the first lsit through the append function
