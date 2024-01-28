from unittest import TestCase

from sample.highscore_lists.highscore_list import HighscoreList


class SimpleHighscoreListListener:
    def list_changed(self, highscore_list: HighscoreList, idx: int) -> None:
        pass


class HighscoreListTest(TestCase):
    def _check_highscore_list(
        self, highscore_list: HighscoreList, elements: list[int]
    ) -> None:
        self.assertEqual(len(elements), highscore_list.size())

        for i, element in enumerate(elements):
            self.assertEqual(element, highscore_list.get_element(i))

    def _add_result_with_listener(self, pos: int, element: int) -> None:
        self.pos1 = pos
        self.highscore_list.add_result(element)
        self.pos2 = (
            (
                self.highscore_list.size()
                - 1
                - self.highscore_list.results[::-1].index(element)
            )
            if element in self.highscore_list.results
            else -1
        )
        self.assertEqual(self.pos1, self.pos2)

    def setUp(self) -> None:
        self.highscore_list = HighscoreList(3)
        self.pos1 = -1
        self.pos2 = -1
        self.listener = SimpleHighscoreListListener()

    def test_constructor(self) -> None:
        self.assertEqual(0, self.highscore_list.size())

    def test_add_element_simple(self) -> None:
        self.highscore_list.add_result(5)
        self._check_highscore_list(self.highscore_list, [5])

        self.highscore_list.add_result(6)
        self._check_highscore_list(self.highscore_list, [5, 6])

        self.highscore_list.add_result(2)
        self._check_highscore_list(self.highscore_list, [2, 5, 6])

    def test_add_element_more_than_max(self) -> None:
        self.highscore_list.add_result(5)
        self.highscore_list.add_result(6)
        self.highscore_list.add_result(2)
        self._check_highscore_list(self.highscore_list, [2, 5, 6])

        self.highscore_list.add_result(3)
        self._check_highscore_list(self.highscore_list, [2, 3, 5])

        self.highscore_list.add_result(7)
        self._check_highscore_list(self.highscore_list, [2, 3, 5])

    def test_add_element_duplicate(self) -> None:
        self.highscore_list.add_result(5)
        self.highscore_list.add_result(6)
        self.highscore_list.add_result(2)
        self._check_highscore_list(self.highscore_list, [2, 5, 6])

        self.highscore_list.add_result(2)
        self._check_highscore_list(self.highscore_list, [2, 2, 5])

    def test_list_listeners_simple(self) -> None:
        self.highscore_list.add_highscore_list_listener(self.listener)

        self._add_result_with_listener(0, 5)
        self._check_highscore_list(self.highscore_list, [5])

        self._add_result_with_listener(1, 6)
        self._check_highscore_list(self.highscore_list, [5, 6])

        self._add_result_with_listener(0, 2)
        self._check_highscore_list(self.highscore_list, [2, 5, 6])

    def test_list_listener_more_than_max(self) -> None:
        self.highscore_list.add_highscore_list_listener(self.listener)

        self.highscore_list.add_result(5)
        self.highscore_list.add_result(6)
        self.highscore_list.add_result(2)
        self._check_highscore_list(self.highscore_list, [2, 5, 6])

        self._add_result_with_listener(1, 3)
        self._check_highscore_list(self.highscore_list, [2, 3, 5])

        self.pos2 = -1
        self._add_result_with_listener(-1, 7)
        self._check_highscore_list(self.highscore_list, [2, 3, 5])

    def test_list_listener_duplicate(self) -> None:
        self.highscore_list.add_highscore_list_listener(self.listener)

        self.highscore_list.add_result(5)
        self.highscore_list.add_result(6)
        self.highscore_list.add_result(2)
        self._check_highscore_list(self.highscore_list, [2, 5, 6])

        self._add_result_with_listener(1, 2)
        self._check_highscore_list(self.highscore_list, [2, 2, 5])
