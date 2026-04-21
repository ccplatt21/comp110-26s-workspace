"""File to define River class."""

from __future__ import annotations
from exercises.ex07.fish import Fish  # routed to exercises not just ex07
from exercises.ex07.bear import Bear

__author__ = "730672284"


class River:

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        # avoid infinite loop issue by creating a new list for survivors
        survivor_fish: list[Fish] = []
        for (
            fish
        ) in (
            self.fish
        ):  # a for loop to go through and check if fish are young enough to survive
            if fish.age <= 3:
                survivor_fish.append(fish)
        self.fish = survivor_fish

        # a list for the survivor bears too
        survivor_bears: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                survivor_bears.append(bear)
        self.bears = survivor_bears

    def remove_fish(self, amount: int) -> None:
        """Remove amount of fish from the front of the list."""
        i: int = 0
        while i < amount:
            self.fish.pop(0)
            i += 1

    def bears_eating(self):
        """Bears eat 3 fish each if there is enough supply."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

    def check_hunger(self):
        """Remove bears with a hunger score below 0."""
        survivor_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                survivor_bears.append(bear)
        self.bears = survivor_bears

    def repopulate_fish(self):
        """EA pair of fish makes 4 more."""
        # got to divide for pairs then multiply by 4
        new_fish: int = int(len(self.fish) / 2) * 4
        i: int = 0
        while i < new_fish:
            self.fish.append(Fish())
            i += 1

    def repopulate_bears(self):
        """Each pair of bears produces 1 kid."""
        new_bears: int = int(len(self.bears) / 2)
        i: int = 0
        while i < new_bears:
            self.bears.append(Bear())
            i += 1

    def __str__(self) -> str:
        """A string representation of the river."""
        return (
            f"~~~ Day {self.day}: ~~~\n"  # \n moves the string to the next line
            f"Fish population: {len(self.fish)}\n"
            f"Bear population: {len(self.bears)}"
        )

    def __add__(self, other_riv: River) -> River:
        """Add the two river objects into one larger river."""
        total_fish: int = len(self.fish) + len(other_riv.fish)
        total_bears: int = len(self.bears) + len(other_riv.bears)
        return River(
            total_fish, total_bears
        )  # return the total of fish and bears of both rivers into the one

    def __mul__(self, factor: int) -> River:
        """Create a new River scaled by a factor"""
        new_fish_count: int = (
            len(self.fish) * factor
        )  # new variables for the scaled up River
        new_bear_count: int = len(self.bears) * factor
        return River(
            new_fish_count, new_bear_count
        )  # return the River with the new scaled up River

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        print(self)

    def one_river_week(self):
        """Call one_river_day 7 times to simulate a week."""
        i: int = 0
        while i < 7:
            self.one_river_day()
            i += 1
