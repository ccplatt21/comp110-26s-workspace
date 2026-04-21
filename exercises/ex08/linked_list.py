from __future__ import annotations


class Node:
    """Node in a singly-linked list recursive structure."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        if self.next is None:
            return f"{self.value} -> None"
        else:
            return f"{self.value} -> {self.next}"


def value_at(head: Node | None, index: int) -> int:
    """Loop through a linked list and identify a specific index."""
    # Edge case of when the list is empty
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    # Base case of when index gets to 0
    if index == 0:
        return head.value
    # Recursive part of this function
    return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Given a head node, return the largest value in the list"""
    # Edge case for empty list
    if head is None:
        raise ValueError("Cannot call max with None")
    # Base case for reaching the end of the list
    if head.next is None:
        return head.value
    # Recursive case to run through and compare to find max value

    # Variable to track largest
    compare_max: int = max(head.next)
    # Loop through and compare each
    if head.value > compare_max:
        return head.value
    else:
        return compare_max


def linkify(items: list[int]) -> Node | None:
    """Given a list of values, return a linked list of nodes."""
    # Base case when list is empty
    if len(items) == 0:
        return None
    # Recursive case building node and adding items using slice
    return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Use a head node and create factored up linked list."""
    # Base case of an empty list
    if head is None:
        return None
    # Recursive case to create a new node with a scaled value and link it to the list
    return Node(head.value * factor, scale(head.next, factor))


courses: Node = Node(110, Node(210, Node(211, None)))
print(courses)
