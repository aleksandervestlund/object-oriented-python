class StopWatch:
    def __init__(self) -> None:
        self.ticks = 0
        self.start_time = -1
        self.stop_time = -1
        self.lap_start_time = -1
        self.lap_time = -1

    def is_started(self) -> bool:
        return self.start_time > -1

    def is_stopped(self) -> bool:
        return self.stop_time > -1

    def tick(self, milli_seconds: int) -> None:
        if milli_seconds < 0:
            raise ValueError("milli_seconds must be positive.")

        self.ticks += milli_seconds

    def lap(self) -> None:
        if not self.is_started():
            raise RuntimeError("StopWatch is not started.")

        if self.lap_start_time > -1:
            self.lap_time = self.ticks - self.lap_start_time

        self.lap_start_time = self.ticks

    def start(self) -> None:
        if self.is_started():
            raise RuntimeError("StopWatch is already started.")

        self.start_time = self.ticks
        self.lap()

    def stop(self) -> None:
        if not self.is_started():
            raise RuntimeError("StopWatch is not started.")
        if self.is_stopped():
            raise RuntimeError("StopWatch is already stopped.")

        self.lap()
        self.stop_time = self.ticks

    def get_time(self) -> int:
        if self.is_stopped():
            return self.stop_time - self.start_time
        if self.is_started():
            return self.ticks - self.start_time
        return -1

    def get_lap_time(self) -> int:
        if self.lap_start_time > -1:
            return self.ticks - self.lap_start_time
        return -1

    def get_last_lap_time(self) -> int:
        return self.lap_time


def main() -> None:
    pass


if __name__ == "__main__":
    main()
