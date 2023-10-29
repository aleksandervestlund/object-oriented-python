from abc import ABC, abstractmethod
from collections.abc import Callable


class Employee(ABC):
    @abstractmethod
    def do_calculations(
        self,
        operation: Callable[[float, float], float],
        value_1: float,
        value_2: float,
    ) -> float:
        pass

    @abstractmethod
    def print_document(self, document: str) -> None:
        pass

    @abstractmethod
    def get_task_count(self) -> int:
        pass

    @abstractmethod
    def get_resource_count(self) -> int:
        pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()
