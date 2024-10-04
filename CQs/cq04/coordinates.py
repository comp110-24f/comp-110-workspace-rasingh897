"""Printing the formatted pairs of each character in the two input strings."""

__author__ = "730809199"


def get_coords(xs: str, ys: str) -> None:
    """This function will print the formatted pairs of the characters in each input string."""
    index1: int = 0
    index2: int = 0
    while index1 < len(xs):
        while index2 < len(ys):
            print("(" + xs[index1] + "," + ys[index2] + ")")
            index2 += 1
        index2 = 0  # resets to 0 so each character can be iterated through
        index1 += 1  # adds 1 to index so that the next character can iterate through


# I probably struggled most with creating this function, however by going out of the nested loop and resetting
# the second index to 0 it can run through all of characters of that string from the beginning again

if __name__ == "__main__":
    get_coords()
