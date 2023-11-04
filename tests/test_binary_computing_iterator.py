from unittest import TestCase
from sample.binary_computing_iterator import BinaryComputingIterator


class TestBinaryComputingIterator(TestCase):
    def setUp(self) -> None:
        self.iterator_1 = iter([0.5, -2.0])
        self.iterator_2 = iter([5.0, 3.0])
        self.iterator_short = iter([5.0])
        self.multiplication_operator = lambda x, y: x * y

    def test_multiplication(self) -> None:
        bci = BinaryComputingIterator(
            self.iterator_1, self.iterator_2, self.multiplication_operator
        )
        self.assertEqual(next(bci), 2.5)
        self.assertEqual(next(bci), -6.0)

    def test_addition(self) -> None:
        bci = BinaryComputingIterator(
            self.iterator_1, self.iterator_2, lambda x, y: x + y
        )
        self.assertEqual(next(bci), 5.5)
        self.assertEqual(next(bci), 1.0)

    def test_short_iterator(self) -> None:
        bci = BinaryComputingIterator(
            self.iterator_1, self.iterator_short, self.multiplication_operator
        )
        self.assertEqual(next(bci), 2.5)

        with self.assertRaises(StopIteration):
            next(bci)

    def test_short_iterator_default(self) -> None:
        bci = BinaryComputingIterator(
            self.iterator_1,
            self.iterator_short,
            self.multiplication_operator,
            default_2=2.0,
        )
        self.assertEqual(next(bci), 2.5)
        self.assertEqual(next(bci), -4.0)

        with self.assertRaises(StopIteration):
            next(bci)

    def test_empty_iterator(self) -> None:
        bci = BinaryComputingIterator(
            iter([]), iter([]), self.multiplication_operator
        )
        with self.assertRaises(StopIteration):
            next(bci)

    def test_empty_iterator_default(self) -> None:
        bci = BinaryComputingIterator(
            iter([]),
            iter([]),
            self.multiplication_operator,
            default_1=1.0,
            default_2=2.0,
        )
        with self.assertRaises(StopIteration):
            next(bci)
