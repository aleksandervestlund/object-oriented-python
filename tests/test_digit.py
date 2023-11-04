from unittest import TestCase
from sample.digit import Digit


class TestDigit(TestCase):
    def test_constructor(self) -> None:
        digit = Digit(10)
        self.assertEqual(digit.value, 0)
        self.assertEqual(digit.base, 10)

        with self.assertRaises(ValueError):
            Digit(-1)

    def _test_digit(
        self, base: int, check_value: bool, check_to_string: bool
    ) -> None:
        digit = Digit(base)
        i = 0
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        while i < base:
            if check_value:
                self.assertEqual(i % base, digit.value)
            if check_to_string:
                self.assertEqual(digits[i % base], repr(digit))

            overflow = digit.increment()
            i += 1

            if check_value:
                self.assertEqual(i % base, digit.value)
                self.assertEqual(i % base == 0, overflow)
            if check_to_string:
                self.assertEqual(digits[i % base], repr(digit))

    def test_increment(self) -> None:
        for base in range(2, 17):
            self._test_digit(base, True, False)

    def test_to_string(self) -> None:
        for base in range(2, 17):
            self._test_digit(base, False, True)
