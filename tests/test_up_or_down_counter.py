from unittest import TestCase

from sample.up_or_down_counter import UpOrDownCounter


class UpOrDownCounterTest(TestCase):
    def _test_count(
        self, counter: UpOrDownCounter, end: int, delta: int
    ) -> None:
        result = True
        while counter.counter < end if delta > 0 else counter.counter > end:
            self.assertTrue(result)
            i = counter.counter
            result = counter.count()
            expected = i + delta
            self.assertEqual(expected, counter.counter)

        self.assertFalse(result)
        self.assertEqual(end, counter.counter)
        self.assertFalse(counter.count())
        self.assertEqual(end, counter.counter)

    def test_up_or_down_counter(self) -> None:
        counter13 = UpOrDownCounter(1, 3)
        self.assertEqual(1, counter13.counter)
        counter31 = UpOrDownCounter(3, 1)
        self.assertEqual(3, counter31.counter)

    def test_up_or_down_counter_with_exception(self) -> None:
        with self.assertRaises(ValueError):
            UpOrDownCounter(0, 0)

    def test_count_up(self) -> None:
        counter13 = UpOrDownCounter(1, 3)
        self._test_count(counter13, 3, 1)

    def test_count_down(self) -> None:
        counter31 = UpOrDownCounter(3, 1)
        self._test_count(counter31, 1, -1)
