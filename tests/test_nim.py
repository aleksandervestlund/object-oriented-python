from unittest import TestCase
from sample.nim import Nim


def check_valid_move(game: Nim, pieces: int, legal: bool) -> bool:
    return (
        legal is game.is_valid_move(pieces, 0)
        and (legal is game.is_valid_move(pieces, 1))
        and (legal is game.is_valid_move(pieces, 2))
    )


class TestNim(TestCase):
    def setUp(self) -> None:
        self.nim = Nim(5)

    def test_constructor(self) -> None:
        self.assertEqual(self.nim.get_pile(0), 5)
        self.assertEqual(self.nim.get_pile(1), 5)
        self.assertEqual(self.nim.get_pile(2), 5)

    def test_remove_pieces(self) -> None:
        self.nim.remove_pieces(3, 0)
        self.nim.remove_pieces(2, 1)
        self.nim.remove_pieces(1, 2)
        self.assertEqual(self.nim.get_pile(0), 2)
        self.assertEqual(self.nim.get_pile(1), 3)
        self.assertEqual(self.nim.get_pile(2), 4)

        with self.assertRaises(ValueError):
            self.nim.remove_pieces(-1, 0)
        with self.assertRaises(ValueError):
            self.nim.remove_pieces(0, 0)
        with self.assertRaises(ValueError):
            self.nim.remove_pieces(3, 0)

    def test_game_over(self) -> None:
        self.assertFalse(self.nim.is_game_over())
        self.nim.remove_pieces(5, 0)
        self.assertEqual(self.nim.get_pile(0), 0)
        self.assertTrue(self.nim.is_game_over())

        with self.assertRaises(ValueError):
            self.nim.remove_pieces(1, 0)
        with self.assertRaises(ValueError):
            self.nim.remove_pieces(1, 1)

    def test_is_valid_move(self) -> None:
        self.assertTrue(check_valid_move(self.nim, 2, True))
        self.assertTrue(check_valid_move(self.nim, -2, False))
        self.assertTrue(check_valid_move(self.nim, 0, False))
        self.assertTrue(check_valid_move(self.nim, 6, False))

        self.nim.remove_pieces(5, 0)
        self.assertTrue(check_valid_move(self.nim, 2, False))
