from unittest import TestCase
from sample.partner import Partner


class TestPartner(TestCase):
    def setUp(self) -> None:
        self.partner_1 = Partner("1")
        self.partner_2 = Partner("2")
        self.partner_3 = Partner("3")
        self.partner_4 = Partner("4")

    def test_constructor(self) -> None:
        self.assertEqual(self.partner_1.name, "1")
        self.assertEqual(self.partner_2.name, "2")
        self.assertIsNone(self.partner_1.partner)
        self.assertIsNone(self.partner_2.partner)

    def test_set_partner_with_self(self) -> None:
        with self.assertRaises(ValueError):
            self.partner_1.set_partner(self.partner_1)

    def test_simple_partnership(self) -> None:
        self.partner_1.set_partner(self.partner_2)
        self.assertEqual(self.partner_1.partner, self.partner_2)
        self.assertEqual(self.partner_2.partner, self.partner_1)

    def test_partnership_with_divorce(self) -> None:
        self.partner_1.set_partner(self.partner_2)
        self.partner_1.set_partner(None)
        self.assertIsNone(self.partner_1.partner)
        self.assertIsNone(self.partner_2.partner)

    def test_swinger(self) -> None:
        self.partner_1.set_partner(self.partner_2)
        self.partner_3.set_partner(self.partner_4)
        self.partner_1.set_partner(self.partner_4)
        self.assertEqual(self.partner_1.partner, self.partner_4)
        self.assertEqual(self.partner_4.partner, self.partner_1)
        self.assertIsNone(self.partner_2.partner)
        self.assertIsNone(self.partner_3.partner)
