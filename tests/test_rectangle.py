from unittest import TestCase
from sample.rectangle import Rectangle


class TestRectangle(TestCase):
    def _assert_values(
        self,
        rectangle: Rectangle,
        min_x: int,
        min_y: int,
        max_x: int,
        max_y: int,
        width: int,
        height: int,
    ) -> None:
        self.assertEqual(rectangle.get_min_x(), min_x)
        self.assertEqual(rectangle.get_min_y(), min_y)
        self.assertEqual(rectangle.get_max_x(), max_x)
        self.assertEqual(rectangle.get_max_y(), max_y)
        self.assertEqual(rectangle.get_width(), width)
        self.assertEqual(rectangle.get_height(), height)

    def _assert_empty(self, rectangle: Rectangle) -> None:
        self.assertTrue(rectangle.is_empty())
        self.assertFalse(rectangle.contains_point(0, 0))
        self.assertTrue(
            rectangle.get_width() == 0 or rectangle.get_height() == 0
        )

    def _test_add(
        self, rectangle: Rectangle, x: int, y: int, expected: bool
    ) -> None:
        self.assertEqual(expected, rectangle.add_point(x, y))
        self.assertFalse(rectangle.is_empty())
        self.assertTrue(rectangle.contains_point(x, y))

    def test_empty(self) -> None:
        rect_1 = Rectangle(0, 0, 0, 0)
        self._assert_empty(rect_1)

        rect_2 = Rectangle(3, 2, 1, 2)
        self._assert_empty(rect_2)

        rect3 = Rectangle(3, 1, 3, 2)
        self._assert_empty(rect3)

    def test_constructor(self) -> None:
        rect_1 = Rectangle(0, 0, 1, 2)
        self._assert_values(rect_1, 0, 0, 1, 2, 1, 2)

        rect_2 = Rectangle(1, 2, 0, 0)
        self._assert_values(rect_2, 0, 0, 1, 2, 1, 2)

        rect3 = Rectangle(3, 3, -1, 5)
        self._assert_values(rect3, -1, 3, 3, 5, 4, 2)

    def test_add_x_y(self) -> None:
        x1 = 13
        y1 = -27
        x2 = -11
        y2 = 23
        x3 = 15
        y3 = 33

        rect = Rectangle(x1, y1, x2, y2)

        self._test_add(rect, x3, y3, True)

        min_x1_x2 = min(x1, x2)
        min_y1_y2 = min(y1, y2)
        max_x1_x2 = max(x1, x2)
        max_y1_y2 = max(y1, y2)
        min_x1_x2_x3 = min(min_x1_x2, x3)
        min_y1_y2_y3 = min(min_y1_y2, y3)
        max_x1_x2_x3 = max(max_x1_x2, x3)
        max_y1_y2_y3 = max(max_y1_y2, y3)

        self._assert_values(
            rect,
            min_x1_x2_x3,
            min_y1_y2_y3,
            max_x1_x2_x3,
            max_y1_y2_y3,
            max_x1_x2_x3 - min_x1_x2_x3,
            max_y1_y2_y3 - min_y1_y2_y3,
        )

    def test_add_same_x_y(self) -> None:
        x1 = 13
        y1 = -27
        x2 = -11
        y2 = 23
        x3 = 15
        y3 = 33

        min_x1_x2 = min(x1, x2)
        min_y1_y2 = min(y1, y2)
        max_x1_x2 = max(x1, x2)
        max_y1_y2 = max(y1, y2)
        min_x1_x2_x3 = min(min_x1_x2, x3)
        min_y1_y2_y3 = min(min_y1_y2, y3)
        max_x1_x2_x3 = max(max_x1_x2, x3)
        max_y1_y2_y3 = max(max_y1_y2, y3)

        rect = Rectangle(x1, y1, x2, y2)

        self._test_add(rect, x3, y3, True)
        self._assert_values(
            rect,
            min_x1_x2_x3,
            min_y1_y2_y3,
            max_x1_x2_x3,
            max_y1_y2_y3,
            max_x1_x2_x3 - min_x1_x2_x3,
            max_y1_y2_y3 - min_y1_y2_y3,
        )

        self._test_add(rect, x3, y3, False)
        self._assert_values(
            rect,
            min_x1_x2_x3,
            min_y1_y2_y3,
            max_x1_x2_x3,
            max_y1_y2_y3,
            max_x1_x2_x3 - min_x1_x2_x3,
            max_y1_y2_y3 - min_y1_y2_y3,
        )

    def test_add_rectangle(self) -> None:
        x1 = 13
        y1 = -27
        x2 = -11
        y2 = 23
        x3 = 15
        y3 = 33

        min_x1_x2 = min(x1, x2)
        min_y1_y2 = min(y1, y2)
        max_x1_x2 = max(x1, x2)
        max_y1_y2 = max(y1, y2)
        min_x1_x3 = min(x1, x3)
        min_y1_y3 = min(y1, y3)
        max_x1_x3 = max(x1, x3)
        max_y1_y3 = max(y1, y3)

        min_x1_x2_x3 = min(min_x1_x2, x3)
        min_y1_y2_y3 = min(min_y1_y2, y3)
        max_x1_x2_x3 = max(max_x1_x2, x3)
        max_y1_y2_y3 = max(max_y1_y2, y3)
        width_x1_x2_x3 = max_x1_x2_x3 - min_x1_x2_x3
        height_x1_x2_x3 = max_y1_y2_y3 - min_y1_y2_y3

        rect = Rectangle(x1, y1, x2, y2)
        self._assert_values(
            rect,
            min_x1_x2,
            min_y1_y2,
            max_x1_x2,
            max_y1_y2,
            max_x1_x2 - min_x1_x2,
            max_y1_y2 - min_y1_y2,
        )

        rect_2 = Rectangle(x1, y1, x3, y3)
        self._assert_values(
            rect_2,
            min_x1_x3,
            min_y1_y3,
            max_x1_x3,
            max_y1_y3,
            max_x1_x3 - min_x1_x3,
            max_y1_y3 - min_y1_y3,
        )

        self.assertTrue(rect.add_rectangle(rect_2))
        self._assert_values(
            rect,
            min_x1_x2_x3,
            min_y1_y2_y3,
            max_x1_x2_x3,
            max_y1_y2_y3,
            width_x1_x2_x3,
            height_x1_x2_x3,
        )

    def test_add_same_rectangle(self) -> None:
        x1 = 13
        y1 = -27
        x2 = -11
        y2 = 23

        width = abs(x1 - x2)
        height = abs(y1 - y2)
        min_x1_x2 = min(x1, x2)
        min_y1_y2 = min(y1, y2)
        max_x1_x2 = max(x1, x2)
        max_y1_y2 = max(y1, y2)

        rect = Rectangle(x1, y1, x2, y2)
        self._assert_values(
            rect, min_x1_x2, min_y1_y2, max_x1_x2, max_y1_y2, width, height
        )

        self.assertFalse(rect.add_rectangle(rect))
        self._assert_values(
            rect, min_x1_x2, min_y1_y2, max_x1_x2, max_y1_y2, width, height
        )

    def test_union(self) -> None:
        x1 = 13
        y1 = -27
        x2 = -11
        y2 = 23
        x3 = 15
        y3 = 33
        x4 = 17
        y4 = -33

        min_x1_x2 = min(x1, x2)
        min_y1_y2 = min(y1, y2)
        max_x1_x2 = max(x1, x2)
        max_y1_y2 = max(y1, y2)
        min_x3_x4 = min(x3, x4)
        min_y3_y4 = min(y3, y4)
        max_x3_x4 = max(x3, x4)
        max_y3_y4 = max(y3, y4)

        rect_1 = Rectangle(x1, y1, x2, y2)
        self._assert_values(
            rect_1,
            min_x1_x2,
            min_y1_y2,
            max_x1_x2,
            max_y1_y2,
            max_x1_x2 - min_x1_x2,
            max_y1_y2 - min_y1_y2,
        )

        rect_2 = Rectangle(x3, y3, x4, y4)
        self._assert_values(
            rect_2,
            min_x3_x4,
            min_y3_y4,
            max_x3_x4,
            max_y3_y4,
            max_x3_x4 - min_x3_x4,
            max_y3_y4 - min_y3_y4,
        )

        min_x = min(min_x1_x2, min_x3_x4)
        min_y = min(min_y1_y2, min_y3_y4)
        max_x = max(max_x1_x2, max_x3_x4)
        max_y = max(max_y1_y2, max_y3_y4)

        union_1 = rect_1.union(rect_2)
        self._assert_values(
            union_1, min_x, min_y, max_x, max_y, max_x - min_x, max_y - min_y
        )
        self._assert_values(
            rect_1,
            min_x1_x2,
            min_y1_y2,
            max_x1_x2,
            max_y1_y2,
            max_x1_x2 - min_x1_x2,
            max_y1_y2 - min_y1_y2,
        )
        self._assert_values(
            rect_2,
            min_x3_x4,
            min_y3_y4,
            max_x3_x4,
            max_y3_y4,
            max_x3_x4 - min_x3_x4,
            max_y3_y4 - min_y3_y4,
        )

        union_2 = rect_2.union(rect_1)
        self._assert_values(
            union_2, min_x, min_y, max_x, max_y, max_x - min_x, max_y - min_y
        )
        self._assert_values(
            rect_1,
            min_x1_x2,
            min_y1_y2,
            max_x1_x2,
            max_y1_y2,
            max_x1_x2 - min_x1_x2,
            max_y1_y2 - min_y1_y2,
        )
        self._assert_values(
            rect_2,
            min_x3_x4,
            min_y3_y4,
            max_x3_x4,
            max_y3_y4,
            max_x3_x4 - min_x3_x4,
            max_y3_y4 - min_y3_y4,
        )

    def test_intersection(self) -> None:
        rect_1 = Rectangle(0, 0, 5, 5)
        rect_2 = Rectangle(3, 3, 7, 7)

        intersection = rect_1.intersection(rect_2)
        self.assertIsNotNone(intersection)
        self._assert_values(intersection, 3, 3, 5, 5, 2, 2)  # type: ignore

        self.assertTrue(rect_1.intersects(rect_2))

    def test_non_intersection(self) -> None:
        rect_1 = Rectangle(-3, -3, 0, 0)
        rect_2 = Rectangle(3, 3, 7, 7)

        intersection = rect_1.intersection(rect_2)
        self.assertIsNone(intersection)
        self.assertFalse(rect_1.intersects(rect_2))
