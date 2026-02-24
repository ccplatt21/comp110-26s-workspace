"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730672284"


def input_word() -> str:
    """a function to prompt the user to enter a 5-character word"""
    word: str = input("Enter a 5-character word: ")

    # now make sure the word is 5 letters exactly and if not, let the user know
    if len(word) != 5:
        print(
            "Error: Word must contain 5 characters."
        )  # print the error for anything other than 5 length
        exit()  # this exits if the user hits the error
    return word  # return the word no matter the length


def input_letter() -> str:
    """a function to prompt the user to enter a single character"""
    letter: str = input("Enter a single character: ")

    # same thing as above just error statement if not a single character
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()  # same thing for exit
    return letter


def contains_char(word: str, letter: str) -> None:
    """a function to check if the letter inputted matches the word"""

    count: int = 0  # the variable to count up the number of matches

    # print the "searching" text in this function
    print(f"Searching for {letter} in {word}")  # f strings make this cleaner

    # now we check the 5 different indices of the 5 letter word (0-4)
    if word[0] == letter:
        print(
            f"{letter} found at index 0"
        )  # print the needed text with an f-string for the letter
        count = count + 1  # this is where the count stacks up per index
    if word[1] == letter:
        print(f"{letter} found at index 1")
        count = (
            count + 1
        )  # only add one each time because it runs linearly and updates as it goes
    if word[2] == letter:
        print(f"{letter} found at index 2")
        count = count + 1
    if word[3] == letter:
        print(f"{letter} found at index 3")
        count = count + 1
    if word[4] == letter:
        print(f"{letter} found at index 4")
        count = count + 1

    # now we need to add if/else statements
    if count == 0:
        print(f"No instances of {letter} found in {word}")
    elif count == 1:
        print(f"1 instance of {letter} found in {word}")  # "instance" here
    else:
        print(f"{count} instances of {letter} found in {word}")  # "instances" here


# need to call main and run everything in order
def main() -> None:
    contains_char(
        word=input_word(), letter=input_letter()
    )  # input functions inside of the function that runs the check


if __name__ == "__main__":
    main()
