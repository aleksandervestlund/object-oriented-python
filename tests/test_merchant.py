from unittest import TestCase
from sample.merchant import Item, Merchant, Types


class TestMerchant(TestCase):
    def setUp(self) -> None:
        self.merchant_1 = Merchant(100.0)
        self.merchant_2 = Merchant(1000.0)
        self.item_1 = Item("Sunveil Katana", Types.WEAPON, 500.0)
        self.item_2 = Item("Carian Greaves", Types.ARMOUR, 100.0)

    def test_constructor(self) -> None:
        self.assertEqual(self.merchant_1.balance, 100.0)
        self.assertEqual(self.merchant_1.inventory, [])

        with self.assertRaises(ValueError):
            Merchant(-1.0)

    def test_obtain_item(self) -> None:
        self.merchant_1.obtain_item(self.item_1)
        self.assertEqual(self.merchant_1.inventory, [self.item_1])
        self.assertEqual(self.item_1.owner, self.merchant_1)

    def test_remove_item(self) -> None:
        self.merchant_1.obtain_item(self.item_1)
        self.merchant_1.remove_item(self.item_1)
        self.assertEqual(self.merchant_1.inventory, [])
        self.assertIsNone(self.item_1.owner)

    def test_sell_item(self) -> None:
        self.merchant_1.obtain_item(self.item_1)
        self.merchant_1.sell_item(self.item_1, self.merchant_2)
        self.assertEqual(self.merchant_1.inventory, [])
        self.assertEqual(self.merchant_1.balance, 600.0)
        self.assertEqual(self.merchant_2.inventory, [self.item_1])
        self.assertEqual(self.merchant_2.balance, 500.0)

        with self.assertRaises(ValueError):
            self.merchant_1.sell_item(self.item_2, self.merchant_2)
        with self.assertRaises(ValueError):
            self.merchant_2.sell_item(self.item_1, self.merchant_2)

        self.merchant_1.balance = 0.0
        with self.assertRaises(ValueError):
            self.merchant_2.sell_item(self.item_1, self.merchant_1)

    def test_item_sale(self) -> None:
        self.merchant_1.obtain_item(self.item_1)
        self.merchant_1.item_sale(0.5, self.item_1)
        self.assertEqual(self.item_1.price, 250.0)

        with self.assertRaises(ValueError):
            self.merchant_1.item_sale(1.5, self.item_1)
        with self.assertRaises(ValueError):
            self.merchant_2.item_sale(0.5, self.item_1)

    def test_inventory_sale(self) -> None:
        self.merchant_1.obtain_item(self.item_1)
        self.merchant_1.obtain_item(self.item_2)
        self.merchant_1.inventory_sale(0.5)
        self.assertEqual(self.item_1.price, 250.0)
        self.assertEqual(self.item_2.price, 50.0)
