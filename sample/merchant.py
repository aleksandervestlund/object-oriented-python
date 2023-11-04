from __future__ import annotations
from enum import Enum, auto
from typing import Self


class Types(Enum):
    WEAPON = auto()
    ARMOUR = auto()
    POTION = auto()
    VALUABLE = auto()


class Item:
    def __init__(self, name: str, type_: Types, price: float) -> None:
        if price < 0.0:
            raise ValueError("Price cannot be negative.")

        self.name = name
        self.type_ = type_
        self._price = price
        self.owner: Merchant | None = None

    def change_owner(self, owner: Merchant | None) -> None:
        self.owner = owner

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, price: float) -> None:
        if price < 0.0:
            raise ValueError("Price cannot be negative.")

        self._price = price

    def __repr__(self) -> str:
        return f"{self.name}: {self.type_.value}, {self.price}."


class Merchant:
    def __init__(self, balance: float) -> None:
        if balance < 0.0:
            raise ValueError("Balance cannot be negative.")

        self.inventory: list[Item] = []
        self.balance = balance

    def obtain_item(self, item: Item) -> None:
        item.change_owner(self)
        self.inventory.append(item)

    def remove_item(self, item: Item) -> None:
        item.change_owner(None)
        self.inventory.remove(item)

    def sell_item(self, item: Item, buyer: Self) -> None:
        item_price = item.price

        if item not in self.inventory:
            raise ValueError("Item unavailable.")
        if item_price > buyer.balance:
            raise ValueError("Buyer has insufficient funds.")
        if buyer is self:
            raise ValueError("Cannot sell to self.")

        buyer.balance -= item_price
        self.balance += item_price
        self.remove_item(item)
        buyer.obtain_item(item)

    def item_sale(self, factor: float, item: Item) -> None:
        if not 0.0 < factor < 1.0:
            raise ValueError("Factor must be between 0 and 1")
        if item.owner is not self:
            raise ValueError("Item is not owned by merchant.")

        item.price *= factor

    def inventory_sale(self, factor: float) -> None:
        for item in self.inventory:
            self.item_sale(factor, item)


def main() -> None:
    i1 = Item("Obsidian Armour", Types.ARMOUR, 199.0)
    print(i1)


if __name__ == "__main__":
    main()
