import math
from unittest import TestCase

from sample.rpn_calc import RPNCalc


class RPNCalcTest(TestCase):
    def setUp(self) -> None:
        self.calc = RPNCalc()

    # This is a custom assertion method.
    def assertIsNan(self, value: float) -> None:
        """Fails if value is not NaN."""
        if not math.isnan(value):
            raise AssertionError(f"{value} is not NaN")

    def test_push(self) -> None:
        self.calc.push(1.0)
        self.assertEqual(1.0, self.calc.peek(0))

        self.calc.push(2.0)
        self.assertEqual(2.0, self.calc.peek(0))

        self.calc.push(3.0)
        self.assertEqual(3.0, self.calc.peek(0))

    def test_pop(self) -> None:
        self.calc.push(1.0)
        self.calc.push(2.0)
        self.calc.push(3.0)
        self.assertEqual(3.0, self.calc.peek(0))

        self.assertEqual(3.0, self.calc.pop())
        self.assertEqual(2.0, self.calc.peek(0))

        self.assertEqual(2.0, self.calc.pop())
        self.assertEqual(1.0, self.calc.peek(0))

        self.calc.push(2.0)
        self.assertEqual(2.0, self.calc.peek(0))

        self.assertEqual(2.0, self.calc.pop())
        self.assertEqual(1.0, self.calc.peek(0))

        self.assertEqual(1.0, self.calc.pop())
        self.assertIsNan(self.calc.pop())

    def test_peek(self) -> None:
        self.calc.push(0.0)
        self.calc.push(1.0)
        self.calc.push(2.0)
        self.assertEqual(2.0, self.calc.peek(0))
        self.assertEqual(1.0, self.calc.peek(1))
        self.assertEqual(0.0, self.calc.peek(2))

    def test_empty_stack(self) -> None:
        self.assertIsNan(self.calc.peek(3))
        self.assertIsNan(self.calc.peek(3))

    def test_add_operation(self) -> None:
        self.calc.push(3.0)
        self.calc.push(4.0)
        self.calc.add_operator("+", lambda x, y: x + y)
        self.calc.perform_operation("+")
        self.assertEqual(7.0, self.calc.peek(0))

    def test_sub_operation(self) -> None:
        self.calc.push(7.0)
        self.calc.push(2.0)
        self.calc.add_operator("-", lambda x, y: x - y)
        self.calc.perform_operation("-")
        self.assertEqual(5.0, self.calc.peek(0))

    def test_mult_operation(self) -> None:
        self.calc.push(5.0)
        self.calc.push(2.0)
        self.calc.add_operator("*", lambda x, y: x * y)
        self.calc.perform_operation("*")
        self.assertEqual(10.0, self.calc.peek(0))

    def test_div_operation(self) -> None:
        self.calc.push(10.0)
        self.calc.push(4.0)
        self.calc.add_operator("/", lambda x, y: x / y)
        self.calc.perform_operation("/")
        self.assertEqual(2.5, self.calc.peek(0))
