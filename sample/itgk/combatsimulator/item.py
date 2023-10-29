from dataclasses import dataclass
from enum import StrEnum, auto


class ItemType(StrEnum):
    OFFENSIVE = auto()
    DEFENSIVE = auto()
    LUCK = auto()
    POTION = auto()


@dataclass(frozen=True, slots=True)
class Item:
    name: str
    type_: ItemType
    power: float

    def __post_init__(self) -> None:
        if self.power < 0:
            raise ValueError("Power must be non-negative")


def main() -> None:
    i_1 = Item("Sword", ItemType.OFFENSIVE, 10)
    print(i_1)

    try:
        Item("Shield", ItemType.DEFENSIVE, -2)
    except ValueError as exception:
        print(exception)

    print(", ".join(ItemType))


if __name__ == "__main__":
    main()
