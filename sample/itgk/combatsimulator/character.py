import random
from typing import Self

from item import Item, ItemType


def _assert_non_negative(amount: float) -> None:
    if amount < 0:
        raise ValueError("Amount must be non-negative")


class Character:
    def __init__(
        self,
        name: str,
        max_hp: float,
        damage: float,
        armor: float,
        luck: float,
        max_mana: float,
    ) -> None:
        self.name = name
        self.max_hp = max_hp
        self.damage = damage
        self.armor = armor
        self.luck = luck
        self.max_mana = max_mana

        self.hp = max_hp
        self.mana = max_mana

        self.potions: list[Item] = []
        self.items: list[Item] = []

    def _luck_roll(self) -> bool:
        return random.randint(0, 99) < self.luck

    def take_damage(self, damage: float) -> None:
        _assert_non_negative(damage)
        if self._luck_roll():
            return

        self.hp -= damage * (200 - self.armor) / 200

    def attack(self, character: Self) -> None:
        if self._luck_roll():
            character.take_damage(2 * self.damage)
        else:
            character.take_damage(self.damage)

    def is_dead(self) -> bool:
        return self.hp <= 0

    def heal(self, amount: float) -> float:
        _assert_non_negative(amount)
        amount = min(self.mana, amount, self.max_hp - self.hp)
        self.mana -= amount
        self.hp += amount
        return amount

    def add_item(self, item: Item) -> None:
        if item.type_ is ItemType.POTION:
            self.potions.append(item)
        else:
            self.items.append(item)

    def restore_mana(self) -> float:
        old_mana = self.mana
        while self.mana < self.max_mana and self.potions:
            potion = self.potions.pop(0)
            self.mana += min(potion.power, self.max_mana - self.mana)
        return self.mana - old_mana


def main() -> None:
    characters: list[Character] = []
    for i in range(1, 3):
        print(f"Character {i}")
        name = input("Name: ")
        max_hp = float(input("Max HP: "))
        damage = float(input("Damage: "))
        armor = float(input("Armor: "))
        luck = float(input("Luck: "))
        max_mana = float(input("Max mana: "))
        print()

        characters.append(
            Character(name, max_hp, damage, armor, luck, max_mana)
        )

    while input("Create an item? [y/n]: ").lower() == "y":
        name = input("Name: ")
        type_ = ItemType[input(f"Type [{'/'.join(ItemType)}]: ").upper()]
        power = float(input("Power: "))
        character = int(input("Character [1/2]: "))
        print()

        characters[character - 1].add_item(Item(name, type_, power))

    actions = ("attack", "heal", "potion")
    to_play = random.randint(0, 1)
    while not any(character.is_dead() for character in characters):
        print(f"Character {to_play + 1}'s turn")

        match input(f"Action [{'/'.join(actions)}]: ").lower():
            case "attack":
                characters[to_play].attack(characters[to_play - 1])
            case "heal":
                print(
                    f"Healed {characters[to_play].heal(float(input('Amount: ')))} "
                    "HP."
                )
            case "potion":
                print(f"Restored {characters[to_play].restore_mana()} mana.")
            case _:
                print("Invalid action")
                print()
                continue

        print()
        to_play = (to_play + 1) % 2

    print(f"Character {characters[to_play - 1].name} won!")


if __name__ == "__main__":
    main()
