from i_logger import ILogger, Severity


class FilteringLogger(ILogger):
    def __init__(self, logger: ILogger) -> None:
        self.logger = logger

        self.logging = {
            Severity.ERROR: False,
            Severity.WARNING: False,
            Severity.INFO: False,
        }

    def is_logging(self, severity: Severity) -> bool:
        return self.logging[severity]

    def set_is_logging(self, severity: Severity, value: bool) -> None:
        if severity not in self.logging:
            raise ValueError(f"Unknown severity {severity}")

        self.logging[severity] = value

    def log(
        self, severity: Severity, message: str, exception: Exception | None
    ) -> None:
        if self.is_logging(severity):
            self.logger.log(severity, message, exception)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
