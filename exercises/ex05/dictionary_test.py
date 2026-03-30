"""Testing the dictionary functions"""

__author__ = "730672284"

from exercises.ex05.dictionary import (
    invert,
    favorite_color,
    count,
    alphabetizer,
    update_attendance,
)
import pytest


# need to use test_ for these
def test_invert_dictionary() -> None:
    """Test the invert function with a dictionary of unique keys and values."""
    dataset: dict[str, str] = {"labrador": "dog", "burmese": "cat"}
    # assert that the function worked to invert the keys and values for this dictionary
    assert invert(dataset) == {"dog": "labrador", "cat": "burmese"}


def test_invert_single_item() -> None:
    """Test invert for one pair."""
    dataset: dict[str, str] = {"Stephen": "Curry"}
    assert invert(dataset) == {"Curry": "Stephen"}


def test_invert_keyerror() -> None:
    """Test that invert raises a KeyError when duplicate values exist."""
    # need to use pytest for this
    with pytest.raises(KeyError):
        dataset: dict[str, str] = {"alyssa": "byrnes", "adam": "byrnes"}
        invert(dataset)


def test_favorite_color_typical() -> None:
    """Test favorite_color with a clear winner."""
    dataset: dict[str, str] = {"Colby": "red", "Nicole": "pink", "John": "red"}
    assert favorite_color(dataset) == "red"


def test_favorite_color_tie() -> None:
    """Test favorite_color returns the first appearing color in a tie."""
    dataset: dict[str, str] = {"Colby": "red", "Nicole": "pink"}
    # Both have 1 vote, but red appeared first in the dictionary
    assert favorite_color(dataset) == "red"


def test_favorite_color_empty() -> None:
    """Test favorite_color with an empty input dictionary."""
    assert favorite_color({}) == ""


def test_count_multiple_items() -> None:
    """Test count with a list that has multiple repeating and unique items."""
    dataset: list[str] = [
        "basketball",
        "football",
        "basketball",
        "soccer",
        "football",
        "basketball",
    ]
    assert count(dataset) == {"basketball": 3, "football": 2, "soccer": 1}


def test_count_all_unique() -> None:
    """Test count where every item in the list appears once and they're unique."""
    dataset: list[str] = ["basketball", "football", "soccer"]
    assert count(dataset) == {"basketball": 1, "football": 1, "soccer": 1}


def test_count_empty() -> None:
    """Test count with an empty input list."""
    assert count([]) == {}


def test_sorting_common_sports() -> None:
    """Test that sports are grouped by their first letter."""
    dataset: list[str] = ["football", "baseball", "basketball", "frisbee"]
    # f gets football and frisbee, and b gets baseball and basketball
    assert alphabetizer(dataset) == {
        "f": ["football", "frisbee"],
        "b": ["baseball", "basketball"],
    }


def test_sports_with_different_cases() -> None:
    """Test that grouping works even if some sports are capitalized."""
    dataset: list[str] = ["Soccer", "softball", "Swimming"]
    # All should still be grouped under lowercase 's'
    assert alphabetizer(dataset) == {"s": ["Soccer", "softball", "Swimming"]}


def test_alphabetizing_empty_sports_list() -> None:
    """Test that an empty list of sports returns an empty dictionary."""
    assert alphabetizer([]) == {}


def test_colby_starts_the_week() -> None:
    """Test adding a student to a day that currently has no attendance."""
    log: dict[str, list[str]] = {}
    update_attendance(log, "Monday", "Colby")
    assert log == {"Monday": ["Colby"]}


def test_nicole_joins_the_team() -> None:
    """Test adding a student to a day that already has students listed."""
    log: dict[str, list[str]] = {"Tuesday": ["Colby"]}
    update_attendance(log, "Tuesday", "Nicole")
    # Nicole should be added to the end of the list for Tuesday
    assert log == {"Tuesday": ["Colby", "Nicole"]}


def test_john_cannot_double_register() -> None:
    """For the edge case, test that the same student isn't added twice to the same day."""
    log: dict[str, list[str]] = {"Wednesday": ["John"]}
    # Try to add John again on the same day
    update_attendance(log, "Wednesday", "John")
    # The list should still only contain John once
    assert log == {"Wednesday": ["John"]}
