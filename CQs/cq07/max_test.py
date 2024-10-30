"""Making test function using pytest"""

__author__ = "730809199"

from CQs.cq07.find_max import find_and_remove_max


def test_find_return1() -> None:
    """use case that ensures function returns expected vale"""
    assert find_and_remove_max(input=[10, 9, 8, 7, 10]) == 10


def test_find_mutate() -> None:
    """use case that ensures function mutates input correctly"""
    test_list = [10, 9, 8, 7, 10]
    assert find_and_remove_max(test_list) == 10
    assert test_list == [9, 8, 7]


def test_find_return2() -> None:
    """edge case that ensures function returns expected value in case of unexpected input"""
    assert find_and_remove_max(input=[]) == -1
