from __future__ import annotations
from enum import Enum, auto


class Gender(Enum):
    MALE = auto()
    FEMALE = auto()


class Person:
    def __init__(self, name: str, gender: Gender) -> None:
        self.name = name
        self.gender = gender
        self._mother: Person | None = None
        self._father: Person | None = None
        self.children: list[Person] = []

    def get_child_count(self) -> int:
        return len(self.children)

    # def __len__(self) -> int:
    #     return len(self.children)

    def get_child(self, n: int) -> Person:
        return self.children[n]

    def add_child(self, child: Person) -> None:
        if child not in self.children:
            self.children.append(child)

        if child.mother is not self and self.gender is Gender.FEMALE:
            child.mother = self
        elif child.father is not self and self.gender is Gender.MALE:
            child.father = self

    def remove_child(self, child: Person) -> None:
        if child in self.children:
            self.children.remove(child)

        if child.father is self:
            child._father = None
        elif child.mother is self:
            child._mother = None

    @property
    def mother(self) -> Person | None:
        return self._mother

    @mother.setter
    def mother(self, mother: Person | None) -> None:
        if mother is not None and mother.gender is not Gender.FEMALE:
            raise ValueError("Mother is male.")
        if mother is self:
            raise ValueError("Cannot be own mother.")

        if self.mother is not None:
            self.mother.remove_child(self)

        self._mother = mother
        if self.mother is not None:
            self.mother.add_child(self)

    @property
    def father(self) -> Person | None:
        return self._father

    @father.setter
    def father(self, father: Person | None) -> None:
        if father is not None and father.gender is not Gender.MALE:
            raise ValueError("Father is female.")
        if father is self:
            raise ValueError("Cannot be own father.")

        if self.father is not None:
            self.father.remove_child(self)

        self._father = father
        if self.father is not None:
            self.father.add_child(self)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
