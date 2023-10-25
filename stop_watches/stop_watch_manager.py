from stop_watches.stop_watch import StopWatch


class StopWatchManager:
    def __init__(self):
        self.stop_watches: dict[str, StopWatch] = {}

    def new_stop_watch(self, name: str) -> StopWatch:
        stop_watch = StopWatch()
        self.stop_watches[name] = stop_watch
        return stop_watch

    def remove_stop_watch(self, name: str) -> None:
        del self.stop_watches[name]

    def tick(self, milli_seconds: int) -> None:
        if milli_seconds < 0:
            raise ValueError("Milliseconds must be positive.")

        for stop_watch in self.stop_watches.values():
            stop_watch.tick(milli_seconds)

    def get_stop_watch(
        self, name: str, throw_exception: bool = False
    ) -> StopWatch | None:
        stop_watch = self.stop_watches.get(name)  # default is None
        if stop_watch is None and throw_exception:
            raise RuntimeError(f"StopWatch '{name}' does not exist.")

        return stop_watch

    def get_watches(
        self, started: bool | None, stopped: bool | None
    ) -> list[StopWatch]:
        watches: list[StopWatch] = []

        for stop_watch in self.stop_watches.values():
            if started is not None and stop_watch.is_started() != started:
                continue
            if stopped is not None and stop_watch.is_stopped() != stopped:
                continue

            watches.append(stop_watch)

        return watches

    def get_all_watches(self) -> list[StopWatch]:
        return list(self.stop_watches.values())
        # return self.get_watches(started=None, stopped=None)

    def get_started_watches(self) -> list[StopWatch]:
        return self.get_watches(started=True, stopped=None)

    def get_stopped_watches(self) -> list[StopWatch]:
        return self.get_watches(started=None, stopped=True)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
