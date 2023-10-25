from office.employee import Employee


class Manager(Employee):
    def __init__(self, employees: list[Employee]) -> None:
        if not employees:
            raise ValueError("At least one employee is required")

        self.employees = employees

        self.iterator = iter(self.employees)
        self.task_count = 0

    def print_document(self, document: str) -> None:
        return self._get_next_employee().print_document(document)

    def get_resource_count(self) -> int:
        return 1 + sum(
            employee.get_resource_count() for employee in self.employees
        )

    def get_task_count(self) -> int:
        return self.task_count

    def _increment_task_count(self) -> None:
        self.task_count += 1

    def do_calculations(self, operation, value_1, value_2) -> float:
        return self._get_next_employee().do_calculations(
            operation, value_1, value_2
        )

    def _get_next_employee(self) -> Employee:
        self._increment_task_count()
        try:
            return next(self.iterator)
        except StopIteration:
            self.iterator = iter(self.employees)
            return next(self.iterator)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
