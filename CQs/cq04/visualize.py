from CQs.cq04.concatenation import concat
from CQs.cq04.coordinates import get_coords

"""Calling concatenation function to visualize it and practice running without importing the whole module."""
# I learned in the lesson that you can also import global variables along with functions from importing.

__author__ = "7301809199"

x: str = "123"
y: str = "abc"
print(concat(x, y))
get_coords(x, y)
