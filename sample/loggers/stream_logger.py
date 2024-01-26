import sys
from typing import TextIO
from sample.loggers.i_logger import ILogger, Severity


class StreamLogger(ILogger):
    def __init__(self, stream: TextIO) -> None:
        self.stream = stream

        self.format_string = "{severity}: {message} ({exception})"

    def log(
        self, severity: Severity, message: str, exception: Exception | None
    ) -> None:
        self.stream.write(
            self.format_string.format(
                severity=severity, message=message, exception=exception
            )
            + "\n"
        )
        self.stream.flush()

    def set_format_string(self, format_string: str) -> None:
        self.format_string = format_string


def main() -> None:
    sl_1 = StreamLogger(sys.stdout)
    sl_1.log(Severity.INFO, "Hello", None)

    with open("sample/loggers/log.txt", "w", encoding="utf-8") as file:
        sl_2 = StreamLogger(file)
        sl_2.log(Severity.WARNING, "Very important", TypeError("TypeError"))


if __name__ == "__main__":
    main()
