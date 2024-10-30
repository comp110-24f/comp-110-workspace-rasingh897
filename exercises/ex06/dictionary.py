"""Exercise to practice dictionary functions"""

__author__ = "730809199"


def invert(input: dict[str, str]) -> dict[str, str]:
    """invert the keys and values of a dictionary"""
    count: int = 0
    output: dict[str, str] = {}
    # returns an error if two values are the same because when inverted two keys will be the same
    for key in input:
        for otherKey in input:
            if input[key] == input[otherKey]:
                count += 1
    if count > len(input):
        raise KeyError("Duplicate keys in dictionary")
    # adds value as the key and key as the value
    for key in input:
        output[input[key]] = key
    return output


def favorite_color(faves: dict[str, str]) -> str:
    """returns the most abundant favorite color"""
    dict_color: dict[str, int] = {}
    empty: str = ""
    if faves == {}:
        return empty
    # makes a dictionary that counts the occurences of each color
    for input in faves:
        color = faves[input]
        if color in dict_color:
            dict_color[color] += 1
        else:
            dict_color[color] = 1
    # section finds most popular color and makes sur first occurence is the return statement
    most_pop: str = ""
    max_count = 0
    for color in dict_color.values():
        if color > max_count:
            max_count = dict_color[color]
            most_pop = color
        elif color == max_count and most_pop is None:
            most_pop = color
    return most_pop


def count(input: list[str]) -> dict[str, int]:
    """Returns a dictionary with keys as inputs of a list and values as number of times occurred in list."""
    dict_count: dict[str, int] = {}
    # empty dictionary to add keys of list and values into
    for word in input:
        if word in dict_count:
            dict_count[word] += 1
            # adds to an existing count if already in the dictionary
        else:
            dict_count[word] = 1
            # creates a new value if not yet occurred
    return dict_count


def alphabetizer(lst: list[str]) -> dict[str, list[str]]:
    """dict where each key is a unique letter in the alphabet and
    each value is a list of the words that begin with that letter."""
    final: dict[str, list[str]] = {}
    for input in lst:
        first = input[0].lower()
        # gets lowercase letter
        if first in final:
            final[first].append(input)
            # add word to the list
        else:
            final[first] = [input]
    return final


def update_attendance(dict: dict[str, list[str]], day: str, student: str) -> None:
    """Mutates dictionary to update attendance."""
    if day in dict:
        # add student to list if not there
        if student not in dict[day]:
            dict[day].append(student)
    else:
        dict[day] = [student]
    return None
