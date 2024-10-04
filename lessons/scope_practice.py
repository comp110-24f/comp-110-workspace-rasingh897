def remove_chars(msg: str, char: str) -> str:
    """Retrun a copy of msg with all instance of char removed."""
    copy: str = ""  # Set up empty str to copy values over
    index: int = 0
    while index < len(msg):
        if msg[index] != char:
            copy += msg[index]
        index += 1
    return copy

if __name__ = "__main__":
    word: str = "yoyo"
    print(remove_chars(word, "o"))
    print(word)
