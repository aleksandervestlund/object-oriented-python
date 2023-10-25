from office.employee import Employee


class Printer:
    def __init__(self) -> None:
        self.print_history: dict[Employee, list[str]] = {}

    def print_document(self, document: str, employee: Employee) -> None:
        self.print_history[employee] = self.get_print_history(employee) + [
            document
        ]
        print(document)

    def get_print_history(self, employee: Employee) -> list[str]:
        return self.print_history.get(employee, [])


def main() -> None:
    pass


if __name__ == "__main__":
    main()
