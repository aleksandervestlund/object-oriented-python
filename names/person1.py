from named import Named


class Person1(Named):
    def __init__(self, given_name: str, family_name: str) -> None:
        super().__init__()
        self.given_name = given_name
        self.family_name = family_name

    def set_given_name(self, given_name: str) -> None:
        self.given_name = given_name

    def get_given_name(self) -> str:
        return self.given_name

    def set_family_name(self, family_name: str) -> None:
        self.family_name = family_name

    def get_family_name(self) -> str:
        return self.family_name

    def set_full_name(self, full_name: str) -> None:
        names = full_name.split(" ")
        if len(names) != 2:
            raise ValueError("Illegal argument.")
        self.given_name, self.family_name = names

    def get_full_name(self) -> str:
        return f"{self.given_name} {self.family_name}"


def main() -> None:
    p1 = Person1("John", "Doe")
    print(p1)

    p1.set_full_name("Jane Doe")
    print(p1)


if __name__ == "__main__":
    main()
