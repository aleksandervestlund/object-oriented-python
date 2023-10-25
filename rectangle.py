from typing import Self


class Rectangle:
    def __init__(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_min_x(self) -> int:
        return min(self.x1, self.x2)

    def get_min_y(self) -> int:
        return min(self.y1, self.y2)

    def get_max_x(self) -> int:
        return max(self.x1, self.x2)

    def get_max_y(self) -> int:
        return max(self.y1, self.y2)

    def get_width(self) -> int:
        return abs(self.x2 - self.x1)

    def get_height(self) -> int:
        return abs(self.y2 - self.y1)

    def is_empty(self) -> bool:
        return self.x1 == self.x2 or self.y1 == self.y2

    def contains_point(self, x: int, y: int) -> bool:
        if self.is_empty():
            return False
        return (
            self.get_min_x() <= x <= self.get_max_x()
            and self.get_min_y() <= y <= self.get_max_y()
        )

    def contains_rectangle(self, rectangle: Self) -> bool:
        return self.contains_point(
            rectangle.x1, rectangle.y1
        ) and self.contains_point(rectangle.x2, rectangle.y2)

    def add_point(self, x: int, y: int) -> bool:
        if self.contains_point(x, y):
            return False
        if x < self.get_min_x():
            if self.x1 == self.get_min_x():
                self.x1 = x
            else:
                self.x2 = x
        elif x > self.get_max_x():
            if self.x2 == self.get_max_x():
                self.x2 = x
            else:
                self.x1 = x

        if y < self.get_min_y():
            if self.y1 == self.get_min_y():
                self.y1 = y
            else:
                self.y2 = y
        elif y > self.get_max_y():
            if self.y2 == self.get_max_y():
                self.y2 = y
            else:
                self.y1 = y
        return True

    def add_rectangle(self, rectangle: Self) -> bool:
        if self.add_point(rectangle.x1, rectangle.y1):
            self.add_point(rectangle.x2, rectangle.y2)
            return True
        return self.add_point(rectangle.x2, rectangle.y2)

    def union(self, rectangle: Self) -> Self:
        return Rectangle(
            min(self.get_min_x(), rectangle.get_min_x()),
            min(self.get_min_y(), rectangle.get_min_y()),
            max(self.get_max_x(), rectangle.get_max_x()),
            max(self.get_max_y(), rectangle.get_max_y()),
        )

    def intersection(self, rectangle: Self) -> Self:
        return Rectangle(
            max(self.get_min_x(), rectangle.get_min_x()),
            max(self.get_min_y(), rectangle.get_min_y()),
            min(self.get_max_x(), rectangle.get_max_x()),
            min(self.get_max_y(), rectangle.get_max_y()),
        )

    def intersects(self, rectangle: Self) -> bool:
        if self.contains_point(
            rectangle.x1, rectangle.y1
        ) or self.contains_point(rectangle.x2, rectangle.y2):
            return True
        if self.contains_point(
            rectangle.x1, rectangle.y2
        ) or self.contains_point(rectangle.x2, rectangle.y1):
            return True
        if rectangle.contains_point(
            self.x1, self.y1
        ) or rectangle.contains_point(self.x2, self.y2):
            return True
        if rectangle.contains_point(
            self.x1, self.y2
        ) or rectangle.contains_point(self.x2, self.y1):
            return True
        return False

    def __repr__(self) -> str:
        return f"Rectangle[({self.x1}),({self.y1}),({self.x2}),({self.y2})]"


def main() -> None:
    pass


if __name__ == "__main__":
    main()
