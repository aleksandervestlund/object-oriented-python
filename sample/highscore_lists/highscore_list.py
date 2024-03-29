from __future__ import annotations
from typing import Protocol


class HighscoreListListener(Protocol):
    def list_changed(self, highscore_list: HighscoreList, idx: int) -> None:
        ...


class HighscoreList:
    def __init__(self, max_size: int) -> None:
        self.max_size = max_size

        self.results: list[int] = []
        self.highscore_list_listeners: list[HighscoreListListener] = []

    def size(self) -> int:
        return len(self.results)

    def get_element(self, index: int) -> int:
        return self.results[index]

    def add_result(self, result: int) -> None:
        if self.size() == self.max_size and result >= self.results[-1]:
            return

        self.results.append(result)
        self.results.sort()

        if self.size() > self.max_size:
            self.results.pop()

        for listener in self.highscore_list_listeners:
            listener.list_changed(
                self, len(self.results) - 1 - self.results[::-1].index(result)
            )

    def add_highscore_list_listener(
        self, listener: HighscoreListListener
    ) -> None:
        if listener not in self.highscore_list_listeners:
            self.highscore_list_listeners.append(listener)

    def remove_highscore_list_listener(
        self, listener: HighscoreListListener
    ) -> None:
        if listener in self.highscore_list_listeners:
            self.highscore_list_listeners.remove(listener)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
