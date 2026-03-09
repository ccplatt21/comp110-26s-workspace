"""Dictionary utility functions assignment."""

__author__ = "730672284"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Invert the keys and values of a given dictionary."""
    # initialize a variable empty list
    result: dict[str, str] = {}

    # Now loop through each of the key/value pairs
    for key in input_dict:
        value = input_dict[key]  # find the value pair for the key
        if value in result:
            raise KeyError(
                "Duplicate key found."
            )  # we raise the Key error if the key is found twice
        # need to invert the key value pair by using the result variable
        else:
            result[value] = key

    return result


def favorite_color(input_dict: dict[str, str]) -> str:
    """Return most popular fav color from name and fav color dict."""
    # need to create a dictionary to count the number of values

    count: dict[str, int] = {}
    for name in input_dict:
        color: str = input_dict[name]  # define color as the value pair to name
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
    """Make a dictionary of the counts of each item in the input list."""
    # establish an empty dictionary to count up all the values
    result: dict[str, int] = {}
    for item in input_list:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1

    return result


def alphabetizer(input_list: list[str]) -> dict[str, list[str]]:
    """Return a list of strings and sort them by letter in alphabet."""
    result: dict[str, list[str]] = {}

    # loop through the different words in the list
    for word in input_list:
        # need to get the first letter of the word and make it lowercase
        first_letter: str = word[0].lower()
        # use an if/else to see if its already in our dictionary, if not, new word
        if first_letter in result:
            result[first_letter].append(word)
        else:
            result[first_letter] = [word]  # brakcets around word to create a new list

    return result


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Add new students to an existing list given the day and student."""
    # first check if the day is in the dictionary yet
    if day in attendance:  # if yes, add student to the existing attendance
        # check for duplicates
        if student not in attendance[day]:
            attendance[day].append(student)
    else:  # if not, make a new list with just that student
        attendance[day] = [student]
