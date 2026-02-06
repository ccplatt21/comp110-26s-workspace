"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730672284"


def input_word() -> str:
    """a function to prompt the user to enter a 5-character word"""
    word: str = input("Enter a 5 character word: ")

    # now make sure the word is 5 letters exactly and if not, let the user know
    if len(word) != 5:
        print(
            "Error: Word must contain 5 letters"
        )  # print the error for anything other than 5 length

    return word  # return the word no matter the length
