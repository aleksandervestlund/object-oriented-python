from collections.abc import Callable

from employee import Employee
from printer import Printer


class Clerk(Employee):
    def __init__(self, printer: Printer) -> None:
        self.printer = printer

        self.task_count = 0

    def _increment_task_count(self) -> None:
        self.task_count += 1

    def do_calculations(
        self,
        operation: Callable[[float, float], float],
        value_1: float,
        value_2: float,
    ) -> float:
        self._increment_task_count()
        return operation(value_1, value_2)

    def print_document(self, document: str) -> None:
        self._increment_task_count()
        self.printer.print_document(document, self)

    def get_task_count(self) -> int:
        return self.task_count

    def get_resource_count(self) -> int:
        return 1


def main() -> None:
    pass


if __name__ == "__main__":
    main()
