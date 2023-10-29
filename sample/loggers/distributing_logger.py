from i_logger import ILogger, Severity


class DistributingLogger(ILogger):
    def __init__(
        self,
        error_logger: ILogger,
        warning_logger: ILogger,
        info_logger: ILogger,
    ) -> None:
        self.error_logger = error_logger
        self.warning_logger = warning_logger
        self.info_logger = info_logger

    def log(
        self, severity: Severity, message: str, exception: Exception | None
    ) -> None:
        if severity is Severity.ERROR:
            self.error_logger.log(severity, message, exception)
        elif severity is Severity.WARNING:
            self.warning_logger.log(severity, message, exception)
        elif severity is Severity.INFO:
            self.info_logger.log(severity, message, exception)

    def set_logger(self, severity: Severity, logger: ILogger) -> None:
        if severity is Severity.ERROR:
            self.error_logger = logger
        elif severity is Severity.WARNING:
            self.warning_logger = logger
        elif severity is Severity.INFO:
            self.info_logger = logger


def main() -> None:
    pass


if __name__ == "__main__":
    main()
