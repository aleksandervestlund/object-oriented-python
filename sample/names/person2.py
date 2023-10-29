from named import Named


class Person2(Named):
    def __init__(self, full_name: str) -> None:
        super().__init__()
        self.full_name = full_name

    def set_given_name(self, given_name: str) -> None:
        self.full_name = f"{given_name} {self.get_family_name()}"

    def get_given_name(self) -> str:
        return self.full_name.split()[0]

    def set_family_name(self, family_name: str) -> None:
        self.full_name = f"{self.get_given_name()} {family_name}"

    def get_family_name(self) -> str:
        return self.full_name.split()[-1]

    def set_full_name(self, full_name: str) -> None:
        self.full_name = full_name

    def get_full_name(self) -> str:
        return self.full_name


def main() -> None:
    p1 = Person2("John Doe")
    print(p1)

    p1.set_full_name("Jane Doe")
    print(p1)


if __name__ == "__main__":
    main()
