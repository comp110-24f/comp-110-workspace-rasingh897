"""Summing the elements of a list using different loops"""

__author__ = "730809199"


def w_sum(vals: list[float]) -> float:
    """returns the sum of a list using a while loop"""
    idx: int = 0
    sum: float = 0.0
    # at first I made the inital sum 0, but upon testing that would make the sum of an
    # empty list an int, by making it a float initially it will return 0.0
    while idx < len(vals):
        sum = sum + vals[idx]
        idx += 1
    return sum


# using a sum local variable in all three functions allows us to add each value in a list
# to a total that can be returned


def f_sum(vals: list[float]) -> float:
    """returns the sum of a list using a for ... in ... loop"""
    sum: float = 0.0
    for nums in vals:
        sum = sum + nums
    return sum


def f_range_sum(vals: list[float]) -> float:
    """returns the sum of a list using a for ... in range ... loop"""
    sum: float = 0.0
    for nums in range(0, len(vals)):
        sum = sum + nums
    return sum


# making the end value of the range the length of list will help if anything is added to the
# list, it will not cause issues for the range being iterated through
