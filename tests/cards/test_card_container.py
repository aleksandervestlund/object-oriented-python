from collections.abc import Iterator
from unittest import TestCase

from sample.cards.card import Card
from sample.cards.card_container import CardContainer, CardContainerIterator


class CardContainerTest(TestCase):
    def setUp(self) -> None:
        self.card_container = CardContainer()
        self.s1 = Card("S", 1)

    def test_get_card_count(self) -> None:
        self.assertEqual(0, self.card_container.get_card_count())
        self.card_container.cards.append(self.s1)
        self.assertEqual(1, self.card_container.get_card_count())

    def test_get_card(self) -> None:
        self.card_container.cards.append(self.s1)
        self.assertEqual(self.s1, self.card_container.get_card(0))
        self.assertEqual(self.s1, self.card_container.get_card(-1))

    def test_iter(self) -> None:
        self.card_container.cards.append(self.s1)
        self.assertIsInstance(iter(self.card_container), Iterator)
        self.assertIsInstance(iter(self.card_container), CardContainerIterator)
        self.assertEqual(self.s1, next(iter(self.card_container)))
