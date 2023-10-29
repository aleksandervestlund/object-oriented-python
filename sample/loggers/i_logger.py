from abc import ABC, abstractmethod
from enum import StrEnum, auto


class Severity(StrEnum):
    INFO = auto()
    WARNING = auto()
    ERROR = auto()


class ILogger(ABC):
    @abstractmethod
    def log(
        self, severity: Severity, message: str, exception: Exception | None
    ) -> None:
        pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()
