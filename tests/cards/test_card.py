from unittest import TestCase

from sample.cards.card_container import Card


class CardTest(TestCase):
    def _check_card(self, card: Card, suit: str, face: int) -> None:
        self.assertEqual(card.suit, suit)
        self.assertEqual(card.face, face)

    def test_constructor(self) -> None:
        self._check_card(Card("S", 1), "S", 1)
        self._check_card(Card("S", 13), "S", 13)
        self._check_card(Card("H", 1), "H", 1)
        self._check_card(Card("H", 13), "H", 13)
        self._check_card(Card("D", 1), "D", 1)
        self._check_card(Card("D", 13), "D", 13)
        self._check_card(Card("C", 1), "C", 1)
        self._check_card(Card("C", 13), "C", 13)

        with self.assertRaises(ValueError):
            Card("X", 1)
        with self.assertRaises(ValueError):
            Card("S", 0)
        with self.assertRaises(ValueError):
            Card("C", 14)

    def test_repr(self) -> None:
        self.assertEqual("S1", repr(Card("S", 1)))
        self.assertEqual("H13", repr(Card("H", 13)))
