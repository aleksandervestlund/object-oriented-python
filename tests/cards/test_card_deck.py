from unittest import TestCase

from sample.cards.card_deck import CardDeck
from sample.cards.card_hand import CardHand


class CardDeckTest(TestCase):
    def _check_deck(self, deck: CardDeck, deck_as_string: str) -> None:
        to_strings = deck_as_string.split(",")
        self.assertEqual(len(to_strings), deck.get_card_count())

        for i, to_string in enumerate(to_strings):
            card = deck.get_card(i)
            card_string = f"{card.suit}{card.face}"
            self.assertEqual(to_string, card_string)

    def setUp(self) -> None:
        self.card_deck = CardDeck(2)

    def test_constructor(self) -> None:
        self._check_deck(self.card_deck, "S1,S2,H1,H2,D1,D2,C1,C2")

    def test_shuffle_perfectly(self) -> None:
        self.card_deck.shuffle_perfectly()
        self._check_deck(self.card_deck, "S1,D1,S2,D2,H1,C1,H2,C2")

    def test_deal(self) -> None:
        hand = CardHand()
        self.card_deck.deal(hand, 3)
        self._check_deck(self.card_deck, "S1,S2,H1,H2,D1")
