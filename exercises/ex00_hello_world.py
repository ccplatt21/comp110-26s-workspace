"""My first exercise in COMP 110!"""

__author__ = 730672284


def greet(name: str) -> str:
    """A welcoming first function definition."""
    return "Hello, " + name + "!"


if __name__ == "__main__":
    print(greet(name=input("What is your name?")))
