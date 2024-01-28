from collections.abc import Iterator
from unittest import TestCase

from sample.cards.card import Card
from sample.cards.card_container import CardContainerIterator
from sample.cards.card_deck import CardDeck


class CardContainerIteratorTest(TestCase):
    def _test_cards(
        self, actual: Iterator[Card], expected: Iterator[Card]
    ) -> None:
        while True:
            try:
                expected_card, actual_card = next(expected), next(actual)
            except StopIteration:
                break
            self.assertEqual(expected_card.suit, actual_card.suit)
            self.assertEqual(expected_card.face, actual_card.face)

    def setUp(self):
        self.iterator = CardContainerIterator(CardDeck(2))
        self.s1 = Card("S", 1)
        self.s2 = Card("S", 2)
        self.h1 = Card("H", 1)
        self.h2 = Card("H", 2)
        self.d1 = Card("D", 1)
        self.d2 = Card("D", 2)
        self.c1 = Card("C", 1)
        self.c2 = Card("C", 2)

    def test_constructor(self):
        self._test_cards(
            self.iterator,
            iter(
                [
                    self.s1,
                    self.s2,
                    self.h1,
                    self.h2,
                    self.d1,
                    self.d2,
                    self.c1,
                    self.c2,
                ]
            ),
        )

    def test_next(self):
        next_card = next(self.iterator)
        self.assertEqual(self.s1.face, next_card.face)
        self.assertEqual(self.s1.suit, next_card.suit)
