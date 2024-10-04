"""Chardle - a cute step towards Wordle."""

__author__ = "730809199"


def main() -> None:
    """main function calls all the other functions at once."""
    contains_char(word=input_word(), letter=input_letter())


def input_word() -> str:
    """Function is used to ask what word to be entered(5 letters) otherwise an error message occurs and module is exited."""
    word_input: str = str(input("Enter a 5-character word: "))
    if len(word_input) == 5:
        return word_input
    else:
        print("Error: Word must contain 5 characters.")
        exit()
        return word_input


def input_letter() -> str:
    """This function serves to ask the user to input a letter, and if it is more than one charcter an error message is given and the module is exited."""
    letter_input: str = str(input("Enter a single character: "))
    if len(letter_input) == 1:
        return letter_input
    else:
        print("Error: Character must be a single character.")
        exit()
        return letter_input


# I was slightly confused for the above two functions on whether or not it was to
# return or print out the word.


def contains_char(word: str, letter: str) -> None:
    """This function is to check if the inputted letter is within the inputted word."""
    # Had a little trouble figuring out how to make the parameters local variables or if
    # that would just be the arguments when calling the function.
    # Accidentally put the if statement and error print output for the single character
    # twice so it printed twice.
    count: int = 0
    print("Searching for " + letter + " in " + word)
    # forgot the space after "for" when running function
    if word[0] == letter:
        print(letter + " found at index 0")
        count = count + 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count = count + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count = count + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count = count + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count = count + 1
    # forgot spaces before "found" when running function
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


# I was initially struggling with how to implement the local variable count because
# working it into the already existing if statements would mean I'd have to repeat
# the "No instances" for error and for 0. So I realized I could just continue making
# conditionals to tie them all together.
# I forgot to put the string of count as count is identified as an integer.


if __name__ == "__main__":
    main()
