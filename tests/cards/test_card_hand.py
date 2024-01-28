from collections.abc import Iterator
from unittest import TestCase

from sample.cards.card_container import Card, CardContainer
from sample.cards.card_hand import CardHand


class CardHandTest(TestCase):
    def setUp(self) -> None:
        self.hand = CardHand()
        self.s1 = Card("S", 1)
        self.c2 = Card("C", 2)
        self.expected = [self.s1, self.c2]

    def _test_cards_container(
        self, it: CardContainer, expected: list[Card]
    ) -> None:
        self.assertEqual(len(expected), it.get_card_count())
        for i, elem in enumerate(expected):
            expected_card = elem
            actual_card = it.get_card(i)
            self.assertEqual(expected_card.suit, actual_card.suit)
            self.assertEqual(expected_card.face, actual_card.face)

    def _test_cards_iterator(
        self, actual: Iterator[Card], expected: Iterator[Card]
    ) -> None:
        while True:
            try:
                expected_card, actual_card = next(expected), next(actual)
            except StopIteration:
                break
            self.assertEqual(expected_card.suit, actual_card.suit)
            self.assertEqual(expected_card.face, actual_card.face)

    def test_card_count(self) -> None:
        self.assertIsInstance(self.hand, CardContainer)
        self.assertEqual(0, self.hand.get_card_count())
        self.hand.add_card(self.s1)
        self.hand.add_card(self.c2)
        self.assertEqual(2, self.hand.get_card_count())

    def test_card_container(self) -> None:
        self.hand.add_card(self.s1)
        self.hand.add_card(self.c2)
        self._test_cards_container(self.hand, self.expected)

    def test_deck_iterator(self) -> None:
        self.hand.add_card(self.s1)
        self.hand.add_card(self.c2)
        self._test_cards_iterator(iter(self.hand), iter(self.expected))
