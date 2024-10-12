"""Mutating functons."""

__author__ = "730809199"


def manual_append(list: list[int], add: int) -> None:
    """adds something (an integer) to a list."""
    list.append(add)


def double(list: list[int]) -> None:
    """Iterates through every index of a list and doubles it."""
    index: int = 0
    while index < len(list):
        list[index] = list[index] * 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list=list_2)
print(list_1)
print(list_2)
# I think list_1 will be printed out as 1,2,3
# I think list_2 will be printed out as 2,4,6
# In the end both were doubled. This is because in the heap only list 1 is stored so if list 2 changes, they both do.
