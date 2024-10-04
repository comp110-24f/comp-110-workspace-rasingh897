"""Returning the concatenation of two input strings."""

__author__ = "730809199"


def concat(input1: str, input2: str) -> str:
    """Function to concatenate two inputs."""
    return input1 + input2


# learned in the lesson that where the if statement is put results in how it is imported
if __name__ == "__main__":
    word1: str = "happy"
    word2: str = "tuesday"
    print(concat(word1, word2))
