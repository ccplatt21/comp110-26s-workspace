"""EX03 - Wordle - An attempt to recreate worldle in python"""

__author__ = "730672284"


def input_guess(secret_word_len: int) -> str:
    """A function to prompt the user and verify guessed len of word to secret word len"""
    guess: str = input(
        f"Enter a {secret_word_len} character word: "
    )  # local variable guess as an input to the prompting

    # a while loop to allow the user to keep guessing if the length doesn't match
    while len(guess) != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")

    return guess


def contains_char(secret_word: str, search_char: str) -> bool:
    """A function to check if the secret word contains the character."""
    assert len(search_char) == 1
    idx: int = 0  # variable to set up for our loop to check indices

    while idx < len(secret_word):
        if secret_word[idx] == search_char:
            return True
        idx += 1

    # If the loop finishes, we checked all indices and found no matches
    return False


# now the emojified function that compares the two strings of the guess and the secret word and returns the emoji str
def emojified(user_guess: str, secret_word: str) -> str:
    """Returning emojis based on how well the user's guess matches the secret word"""
    assert len(user_guess) == len(secret_word)
    WHITE_BOX: str = "\U00002b1c"
    GREEN_BOX: str = "\U0001f7e9"
    YELLOW_BOX: str = "\U0001f7e8"

    # Now we need to create a loop to go through, select emojis, and then concatenate them into a str
    emoji: str = ""  # emoji variable starts us with an empty string
    idx: int = 0  # this index variable helps us run the while loop

    # a while loop to loop throguh each index and emojify
    while idx < len(user_guess):
        if (
            user_guess[idx] == secret_word[idx]
        ):  # if the letters at that index match, green box
            emoji += GREEN_BOX  # assignment operator to add the green box to the emoji variable empty string
        elif contains_char(
            secret_word, user_guess[idx]
        ):  # if the letters match somewhere else, yellow box
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
        idx += 1  # Assignment operator to make sure the loop goes through all indices
    return emoji  # return the emoji so it can be printed


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    # What variables to keep track of? current turn and if they've won
    n: int = 1  # variable for turn
    win: bool = False  # a bool for if they've won starting at False

    while (
        n <= 6 and win == False
    ):  # the loop continues up to 6 turns and if they haven't won
        # first print f-string to show the turn number
        print(f"=== Turn {n}/6 ===")
        # run our loop from secret_word_len and then store it locally as "guess"
        guess: str = input_guess(secret_word_len=len(secret))
        # print the emojis based on the guess that the user makes
        print(emojified(user_guess=guess, secret_word=secret))
        # if statement for if they won
        if guess == secret:
            win = True
        n += 1

    # Now an if/else to print based on if the user won or not and in how many turns
    if win == True:
        print(f"You won in {n - 1}/6 turns!")
    else:
        print(f"X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
