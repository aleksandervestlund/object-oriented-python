from unittest import TestCase

from sample.string_merging_iterator import StringMergingIterator


class StringMergingIteratorProgram(TestCase):
    def setUp(self) -> None:
        self.string_merging_iterator = StringMergingIterator(
            iter(["a", "b"]), iter(["c", "d", "e"])
        )

    def test_next(self) -> None:
        self.assertEqual("a", next(self.string_merging_iterator))
        self.assertEqual("c", next(self.string_merging_iterator))
        self.assertEqual("b", next(self.string_merging_iterator))
        self.assertEqual("d", next(self.string_merging_iterator))
        self.assertEqual("e", next(self.string_merging_iterator))

        with self.assertRaises(StopIteration):
            next(self.string_merging_iterator)
