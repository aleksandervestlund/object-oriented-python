from abc import ABC, abstractmethod


class Named(ABC):
    @abstractmethod
    def set_given_name(self, given_name: str) -> None:
        pass

    @abstractmethod
    def get_given_name(self) -> str:
        pass

    @abstractmethod
    def set_family_name(self, family_name: str) -> None:
        pass

    @abstractmethod
    def get_family_name(self) -> str:
        pass

    @abstractmethod
    def set_full_name(self, full_name: str) -> None:
        pass

    @abstractmethod
    def get_full_name(self) -> str:
        pass

    def __repr__(self) -> str:
        return self.get_full_name()


def main() -> None:
    pass


if __name__ == "__main__":
    main()
