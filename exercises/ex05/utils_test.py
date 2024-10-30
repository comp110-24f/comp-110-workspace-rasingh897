"""Unit tests for each utils function with one edge and two use cases."""

__author__ = "730809199"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import add_at_index
import pytest


def test_only_evens_list() -> None:
    """tests that the only_evens function doesn't modify or mutate the original input"""
    test_list = [1, 2, 3, 4]
    assert only_evens(input=test_list) == [2, 4]
    assert test_list == [1, 2, 3, 4]


def test_only_evens_return() -> None:
    """tests that the only_evens function returns a new list with only even integers"""
    assert only_evens(input=[4, 6, 7, 9]) == [4, 6]


def test_only_evens_empty() -> None:
    """tests that an empty input into the only_evens function will return an empty list"""
    assert only_evens(input=[]) == []


def test_sub_list() -> None:
    """Tests that the sub function doesn't modify or mutate the original enter list"""
    tst = [40, 50, 70, 80]
    assert sub(tst, 1, 3) == [50, 70]
    assert tst == [40, 50, 70, 80]
    # because the return type is none, we can't assert the function equals the list, rather we implement the function
    # and check that the test gets mutated by asserting the list is equal to what we want


def test_sub_return() -> None:
    """Tests that the sub function correctly returns a subset of the input"""
    tst = [50, 90, 80, 20, 60, 90]
    assert sub(tst, 3, 5) == [20, 60]


def test_sub_start_length() -> None:
    """Tests that if the start index is greater than the length of the list, returns an empty list"""
    tst = [20, 40, 80, 90, 30]
    assert sub(tst, 5, 3) == []
    # 5 is out of range for the index so it will return the empty list


def test_add_at_index_error():
    """Tests that there is an IndexError raised if list is out of range."""
    with pytest.raises(IndexError):
        add_at_index([1, 2, 3, 4], 4, 5)
        # your object to pass to add_at_index function
        # an IndexError is raised for the case when the add_at_index is given an <index_to_insert_num>
        # that is greater than the length of our <list_object>


def test_add_at_index_return() -> None:
    """Tests that add_at_index will add a value at the index given to the list"""
    tst: list[int] = [30, 30, 6, 8, 10]
    add_at_index(tst, 3, 2)
    assert tst == [30, 30, 3, 6, 8, 10]


def test_add_at_index_new() -> None:
    """Tests that a new index will be added to the end of the list to add a value at the index"""
    tst = [1, 5]
    add_at_index(tst, 4, 2)
    assert tst == [1, 5, 4]
