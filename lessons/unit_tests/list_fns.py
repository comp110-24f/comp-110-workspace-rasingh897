"""Testing different functions"""


def get_first(input: list[str]) -> str:
    """ "returns first element of a list"""
    return input[0]


def remove_first(input: list[str]) -> None:
    """Pop first element off a list"""
    input.pop(0)


def get_and_remove_first(input: list[str]) -> str:
    """Returns first element and pops it off!!!"""
    first: str = input[0]
    input.pop(0)
    return first
