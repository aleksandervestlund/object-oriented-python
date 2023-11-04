from unittest import TestCase
from sample.line_editor import LineEditor


class TestLineEditor(TestCase):
    def setUp(self) -> None:
        self.line_editor = LineEditor()

    def test_constructor(self) -> None:
        self.assertEqual(self.line_editor.text, "")
        self.assertEqual(self.line_editor.insertion_index, 0)

    def test_text(self) -> None:
        self.line_editor.text = "ABC"
        self.assertEqual(self.line_editor.text, "ABC")

        self.line_editor.text = ""
        self.assertEqual(self.line_editor.text, "")

    def test_insertion_index(self) -> None:
        self.line_editor.text = "ABC"
        self.assertEqual(self.line_editor.insertion_index, 3)

        self.line_editor.insertion_index = 0
        self.assertEqual(self.line_editor.insertion_index, 0)

        with self.assertRaises(ValueError):
            self.line_editor.insertion_index = -1

        with self.assertRaises(ValueError):
            self.line_editor.insertion_index = 4

    def test_left(self) -> None:
        self.line_editor.text = "ABC"
        self.line_editor.left()
        self.assertEqual(self.line_editor.insertion_index, 2)

        self.line_editor.left()
        self.assertEqual(self.line_editor.insertion_index, 1)

        self.line_editor.left()
        self.assertEqual(self.line_editor.insertion_index, 0)

        self.line_editor.left()
        self.assertEqual(self.line_editor.insertion_index, 0)

    def test_right(self) -> None:
        self.line_editor.text = "ABC"
        self.line_editor.insertion_index = 0
        self.line_editor.right()
        self.assertEqual(self.line_editor.insertion_index, 1)

        self.line_editor.right()
        self.assertEqual(self.line_editor.insertion_index, 2)

        self.line_editor.right()
        self.assertEqual(self.line_editor.insertion_index, 3)

        self.line_editor.right()
        self.assertEqual(self.line_editor.insertion_index, 3)

    def test_delete_left(self) -> None:
        self.line_editor.text = "ABC"
        self.line_editor.insertion_index = 0
        self.line_editor.delete_left()
        self.assertEqual(self.line_editor.text, "ABC")
        self.assertEqual(self.line_editor.insertion_index, 0)

        self.line_editor.insertion_index = 1
        self.line_editor.delete_left()
        self.assertEqual(self.line_editor.text, "BC")
        self.assertEqual(self.line_editor.insertion_index, 0)
        self.line_editor.delete_left()
        self.assertEqual(self.line_editor.text, "BC")
        self.assertEqual(self.line_editor.insertion_index, 0)

        self.line_editor.insertion_index = 2
        self.line_editor.delete_left()
        self.assertEqual(self.line_editor.text, "B")
        self.assertEqual(self.line_editor.insertion_index, 1)

        self.line_editor.delete_left()
        self.assertEqual(self.line_editor.text, "")
        self.line_editor.delete_left()
        self.assertEqual(self.line_editor.text, "")

    def test_delete_right(self) -> None:
        self.line_editor.text = "ABC"
        self.line_editor.delete_right()
        self.assertEqual(self.line_editor.text, "ABC")
        self.assertEqual(self.line_editor.insertion_index, 3)

        self.line_editor.insertion_index = 2
        self.line_editor.delete_right()
        self.assertEqual(self.line_editor.text, "AB")
        self.assertEqual(self.line_editor.insertion_index, 2)
        self.line_editor.delete_right()
        self.assertEqual(self.line_editor.text, "AB")
        self.assertEqual(self.line_editor.insertion_index, 2)

        self.line_editor.insertion_index = 0
        self.line_editor.delete_right()
        self.assertEqual(self.line_editor.text, "B")
        self.assertEqual(self.line_editor.insertion_index, 0)

        self.line_editor.delete_right()
        self.assertEqual(self.line_editor.text, "")
        self.line_editor.delete_right()
        self.assertEqual(self.line_editor.text, "")

    def test_insert_string(self) -> None:
        self.line_editor.text = "ABC"
        self.line_editor.insert_string("DEF")
        self.assertEqual(self.line_editor.text, "ABCDEF")
        self.assertEqual(self.line_editor.insertion_index, 6)

        self.line_editor.insertion_index = 0
        self.line_editor.insert_string("GHI")
        self.assertEqual(self.line_editor.text, "GHIABCDEF")
        self.assertEqual(self.line_editor.insertion_index, 3)

        self.line_editor.insertion_index = 3
        self.line_editor.insert_string("JKL")
        self.assertEqual(self.line_editor.text, "GHIJKLABCDEF")
        self.assertEqual(self.line_editor.insertion_index, 6)
