"""File to define Fish class."""

__author__ = "730672284"


class Fish:

    age: int

    def __init__(self):
        """Initialize the fish's age with 0."""
        self.age = 0

    def one_day(self):
        """Increases age by 1."""
        self.age += 1
