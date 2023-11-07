from unittest import TestCase
from sample.person import Person, Gender


class TestPerson(TestCase):
    def setUp(self) -> None:
        self.person_1 = Person("Hallvard", Gender.MALE)
        self.person_2 = Person("Marit", Gender.FEMALE)
        self.person_3 = Person("Jens", Gender.MALE)
        self.person_4 = Person("Marit", Gender.FEMALE)

    def _has_children(self, person: Person, children: list[Person]) -> None:
        self.assertEqual(len(children), person.get_child_count())
        for child in children:
            self.assertIn(child, person.children)

    def test_illegal_set_mothers(self) -> None:
        with self.assertRaises(ValueError):
            self.person_3.mother = self.person_1
        with self.assertRaises(ValueError):
            self.person_2.mother = self.person_2

    def test_illegal_set_fathers(self) -> None:
        with self.assertRaises(ValueError):
            self.person_3.father = self.person_2
        with self.assertRaises(ValueError):
            self.person_1.father = self.person_1

    def test_set_father(self) -> None:
        self.person_3.father = self.person_1

        self.assertIsNone(self.person_1.father)
        self.assertIsNone(self.person_1.mother)
        self._has_children(self.person_1, [self.person_3])

        self.assertEqual(self.person_3.father, self.person_1)
        self.assertIsNone(self.person_3.mother)
        self.assertEqual(self.person_3.get_child_count(), 0)

        self.person_4.father = self.person_1

        self.assertIsNone(self.person_1.father)
        self.assertIsNone(self.person_1.mother)
        self._has_children(self.person_1, [self.person_3, self.person_4])

        self.assertEqual(self.person_3.father, self.person_1)
        self.assertIsNone(self.person_3.mother)
        self.assertEqual(self.person_3.get_child_count(), 0)

        self.assertEqual(self.person_4.father, self.person_1)
        self.assertIsNone(self.person_4.mother)
        self.assertEqual(self.person_4.get_child_count(), 0)

    def test_father_add_child(self) -> None:
        self.person_1.add_child(self.person_3)

        self.assertIsNone(self.person_1.father)
        self.assertIsNone(self.person_1.mother)
        self._has_children(self.person_1, [self.person_3])

        self.assertEqual(self.person_3.father, self.person_1)
        self.assertIsNone(self.person_3.mother)
        self.assertEqual(self.person_3.get_child_count(), 0)

        self.person_1.add_child(self.person_4)

        self.assertIsNone(self.person_1.father)
        self.assertIsNone(self.person_1.mother)
        self._has_children(self.person_1, [self.person_3, self.person_4])

        self.assertEqual(self.person_3.father, self.person_1)
        self.assertIsNone(self.person_3.mother)
        self.assertEqual(self.person_3.get_child_count(), 0)

        self.assertEqual(self.person_4.father, self.person_1)
        self.assertIsNone(self.person_4.mother)
        self.assertEqual(self.person_4.get_child_count(), 0)

    def test_set_mother(self) -> None:
        self.person_3.mother = self.person_2

        self.assertIsNone(self.person_2.father)
        self.assertIsNone(self.person_2.mother)
        self._has_children(self.person_2, [self.person_3])

        self.assertIsNone(self.person_3.father)
        self.assertEqual(self.person_3.mother, self.person_2)
        self.assertEqual(self.person_3.get_child_count(), 0)

        self.person_4.mother = self.person_2

        self.assertIsNone(self.person_2.father)
        self.assertIsNone(self.person_2.mother)
        self._has_children(self.person_2, [self.person_3, self.person_4])

        self.assertIsNone(self.person_3.father)
        self.assertEqual(self.person_3.mother, self.person_2)
        self.assertEqual(self.person_3.get_child_count(), 0)

        self.assertIsNone(self.person_4.father)
        self.assertEqual(self.person_4.mother, self.person_2)
        self.assertEqual(self.person_4.get_child_count(), 0)

    def test_mother_add_child(self) -> None:
        self.person_2.add_child(self.person_3)

        self.assertIsNone(self.person_2.father)
        self.assertIsNone(self.person_2.mother)
        self._has_children(self.person_2, [self.person_3])

        self.assertIsNone(self.person_3.father)
        self.assertEqual(self.person_3.mother, self.person_2)
        self.assertEqual(self.person_3.get_child_count(), 0)

        self.person_2.add_child(self.person_4)

        self.assertIsNone(self.person_2.father)
        self.assertIsNone(self.person_2.mother)
        self._has_children(self.person_2, [self.person_3, self.person_4])

        self.assertIsNone(self.person_3.father)
        self.assertEqual(self.person_3.mother, self.person_2)
        self.assertEqual(self.person_3.get_child_count(), 0)

        self.assertIsNone(self.person_4.father)
        self.assertEqual(self.person_4.mother, self.person_2)
        self.assertEqual(self.person_4.get_child_count(), 0)

    def test_change_father_set_father(self) -> None:
        self.person_4.father = self.person_3
        self.person_4.father = self.person_1

        self.assertEqual(self.person_4.father, self.person_1)
        self.assertEqual(self.person_3.get_child_count(), 0)
        self._has_children(self.person_1, [self.person_4])

    def test_change_father_add_child(self) -> None:
        self.person_3.add_child(self.person_4)
        self.person_1.add_child(self.person_4)

        self.assertEqual(self.person_4.father, self.person_1)
        self.assertEqual(self.person_3.get_child_count(), 0)
        self._has_children(self.person_1, [self.person_4])

    def test_change_mother_set_mother(self) -> None:
        self.person_3.mother = self.person_4
        self.person_3.mother = self.person_2

        self.assertEqual(self.person_3.mother, self.person_2)
        self.assertEqual(self.person_4.get_child_count(), 0)
        self._has_children(self.person_2, [self.person_3])

    def test_change_mother_add_child(self) -> None:
        self.person_4.add_child(self.person_3)
        self.person_2.add_child(self.person_3)

        self.assertEqual(self.person_3.mother, self.person_2)
        self.assertEqual(self.person_4.get_child_count(), 0)
        self._has_children(self.person_2, [self.person_3])
