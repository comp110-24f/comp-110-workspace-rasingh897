"""Creating functions to be tested using pytest"""

__author__ = "730809199"


def find_and_remove_max(input: list[int]) -> int:
    """Function that will find and remove the largest integer in the list."""
    if len(input) == 0:
        return -1
    max: int = input[0]
    idx: int = 0
    while idx < len(input):
        if max < input[idx]:
            max = input[idx]
        idx += 1
    idx = 0
    while idx < len(input):
        if max == input[idx]:
            input.pop(idx)
        else:
            idx += 1
    return max
