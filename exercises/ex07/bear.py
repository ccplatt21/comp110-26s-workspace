"""File to define Bear class."""

__author__ = "730672284"


class Bear:
    """Bear in da river."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initialize the bear's age and hunger to 0."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self):
        """Increase age by 1 and lower hunger by 1."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int):
        """Increase hunger score by number of fish eaten."""
        self.hunger_score += num_fish
