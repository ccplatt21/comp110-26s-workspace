"""Dictionary utility functions assignment"""

__author__ = "730672284"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a given dictionary"""
    # initialize a variable empty list
    Result: dict[str, str] = {}

    # Now loop through each of the key/value pairs
    for key in input:
        value = input[key]  # find the value pair for the key
        if value in Result:
            raise KeyError(
                "duplicate key found"
            )  # we raise the Key error if the key is found twice
        # need to invert the key value pair by using the result variable
        else:
            Result[value] = key

    return Result


def favorite_color(input: dict[str, str]) -> str:
    """Takes names and fav color and returns most popular fav color"""
    # need to create a dictionary to count the number of values

    count: dict[str, int] = {}
    for name in input:
        color: str = input[name]  # define color as the value pair to name
        if color in count:
            count[color] += 1
        else:
            count[color] = 1

    # initialize some new variables to track
    max_count: int = 0
    popular_color: str = ""
    # a for loop to loop through all the different color counts
    for color in count:
        # if the count for a color is the biggest, update the number and color name
        if count[color] > max_count:
            popular_color = color
            max_count = count[color]

    return popular_color


def count(input_list: list[str]) -> dict[str, int]:
    """taking a list and turning it into a dictionary of frequencies the strings appear"""
    # establish an empty dictionary to count up all the values
    Result: dict[str, int] = {}
    for item in input_list:
        if item in Result:
            Result[item] += 1
        else:
            Result[item] = 1

    return Result


def alphabetizer(input_list: list[str]) -> dict[str, list[str]]:
    """takes a list of strings and sorts them by letter in alphabet"""
    Result: dict[str, list[str]] = {}

    # loop through the different words in the list
    for word in input_list:
        # need to get the first letter of the word and make it lowercase
        first_letter: str = word[0].lower()
        # use an if/else to see if its already in our dictionary, if not, new word
        if first_letter in Result:
            Result[first_letter].append(word)
        else:
            Result[first_letter] = [word]  # brakcets around word to create a new list

    return Result


    def update_attendance(attendance: dict[str], list[str], student: str, day: str)-> None: 
        """Add new students to an existing list given the day and student"""

