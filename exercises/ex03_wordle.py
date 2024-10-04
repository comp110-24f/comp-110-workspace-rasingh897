"""Creating a wordle using loops and codified emojis."""

__author__ = "730809199"


def input_guess(secret_word_len: int) -> str:
    """This function is to make sure the inputted word matches the length of the secret word."""
    word_input: str = str(input(f"Enter a {secret_word_len} character word: "))
    while len(word_input) != secret_word_len:
        word_input = str(input(f"That wasn't {secret_word_len} chars! Try again: "))
    return word_input


# I got confused on how to change the input and rerun and realized I could update the word_input variable
# and have it ask for another input with the prompt given from the instructions
# the f-string is so cool


def contains_char(secret_word: str, char_guess: str) -> bool:
    """This function is going to search for a letter within a word."""
    assert len(char_guess) == 1
    index: int = 0
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            return True
        index = index + 1
    else:
        return False


# It was much easier being able to build this function with a loop in contrast to chardle


def emojified(guess: str, secret: str) -> str:
    """Check an inputted guess to see if any characters match the secret and return a code of emojis to explain matching characters."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    return_call: str = ""
    index: int = 0
    # I can reuse the index name for the variable since it is a local variable
    while index < len(guess):
        if guess[index] == secret[index]:
            return_call += GREEN_BOX
        elif contains_char(secret_word=secret, char_guess=guess[index]) == True:
            return_call += YELLOW_BOX
        else:
            return_call += WHITE_BOX
        index += 1
    return return_call


# initially my results would be printed horizontally, I realized I needed to make a local variable
# starting at an empty string in order to add on the results of the function and return the whole thing at the end


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    win: bool = False
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        guessed_word: str = input_guess(secret_word_len=len(secret))
        response: str = emojified(guess=guessed_word, secret=secret)
        # by creating a local variable I can use it in the conditional
        # I struggled with this section but making the variables is what makes it easier to call
        # the arguments when needed
        print(response)
        if guessed_word == secret:
            print(f"You won in {turn}/6 turns!")
            return
        else:
            turn += 1
    print(f"{turn}/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
