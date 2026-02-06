"""A Program to Plan My Tea Party"""

__author__: str = "730672284"


def main_planner(guests: int) -> None:
    """Brings amount of tea bags, treats, and cost together from number of guests!"""

    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Calculating # tea bags for # people attending party"""
    return 2 * people


def treats(people: int) -> int:
    """Calculating # of treats for # of people attending party"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculating the cost based on number of teas and treats"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
