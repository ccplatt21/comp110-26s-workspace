class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """Return a string representation for point."""
        return f"Point storing: ({self.x}, {self.y})"

    def __repr__(self) -> str:
        """Return a string representation for debugging purposes"""
        return f"Point({self.x}, {self.y})"

    def dist_from_origin(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def translate_x(self, dx: float) -> None:
        self.x += dx

    def translate_y(self, dy: float) -> None:
        self.y += dy


pt: Point = Point(2.0, 1.0)


class Line:
    start: Point
    end: Point

    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def __str__(self) -> str:
        """Provide the start and end points of Line"""
        return f"Line from {self.start} to {self.end}"

    def __repr__(self) -> str:
        return f"Line({repr(self.start)}, {repr(self.end)})"

    def get_length(self) -> float:
        return (
            (self.end.x - self.start.x) ** 2 + (self.end.y - self.start.y) ** 2
        ) ** 0.5

    def get_slope(self) -> float:
        return (self.end.y - self.start.y) / (self.end.x - self.start.x)


old_well: Point = Point(2.0, 1.0)
morehead_plan: Point = Point(7.0, 5.0)
ow_to_morehead: Line = Line(old_well, morehead_plan)
print(old_well)
print(ow_to_morehead)
