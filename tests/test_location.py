from unittest import TestCase
from sample.location import Location


class TestLocation(TestCase):
    def setUp(self) -> None:
        self.location = Location()

    def test_constructor(self) -> None:
        self.assertEqual(self.location.x, 0)
        self.assertEqual(self.location.y, 0)

    def test_up(self) -> None:
        self.location.up()
        self.assertEqual(self.location.y, -1)

        self.location.up()
        self.assertEqual(self.location.y, -2)

    def test_down(self) -> None:
        self.location.down()
        self.assertEqual(self.location.y, 1)

        self.location.down()
        self.assertEqual(self.location.y, 2)

    def test_left(self) -> None:
        self.location.left()
        self.assertEqual(self.location.x, -1)

        self.location.left()
        self.assertEqual(self.location.x, -2)

    def test_right(self) -> None:
        self.location.right()
        self.assertEqual(self.location.x, 1)

        self.location.right()
        self.assertEqual(self.location.x, 2)

    def test_complex_movement(self) -> None:
        for _ in range(9):
            self.location.down()
        for _ in range(11):
            self.location.right()

        self.assertEqual(self.location.x, 11)
        self.assertEqual(self.location.y, 9)
