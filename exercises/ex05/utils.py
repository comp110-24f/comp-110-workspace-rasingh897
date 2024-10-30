"""Writing list utility functions to be tested with unit tests."""

__author__ = "730809199"


def only_evens(input: list[int]) -> list[int]:
    """returns only the evens of a given list without modifying the list."""
    new_list: list[int] = []
    # creating a seperate local variable will ensure that the original list won't be mutated, instead
    # a seperate list will be made of only evens
    for nums in input:
        if nums % 2 == 0:
            new_list.append(nums)
    return new_list


def sub(enter: list[int], start: int, end: int) -> list[int]:
    """returns a list which is a subset of the list between start and end index minus one."""
    subset: list[int] = []
    idx: int = start
    if start < 0:
        idx = 0
    if end > len(enter):
        end = len(enter)
    if len(enter) == 0 or start >= len(enter) or end == 0:
        return subset
    # using the or makes it easier to simplify all the statements on one line as they all return
    while idx < end:
        subset.append(enter[idx])
        idx += 1
        # using the while loop, the idx will iterate through the values from the start index and add those to a seperate list
        # this will ensure the original list won't be modified
    return subset


def add_at_index(input: list[int], add: int, index: int) -> None:
    if index < 0 or index > len(input):
        raise IndexError("Index is out of bounds for the input list")
    input.append(0)
    count = len(input) - 1
    # starting the count from here will make sure it starts from the last integer of the list
    while count > index:
        input[count] = input[count - 1]
        # this will set the integer at that index to the integer of the previous index
        # initially I had the -1 outside the bracket but that would make it -1
        count -= 1
    input[index] = add
