from typing import Protocol

from sample.observable_highscore_lists.observable_list import ObservableList


class ObservableListListener(Protocol):
    def list_changed(self, source: ObservableList, idx: int) -> None:
        ...


def main() -> None:
    pass


if __name__ == "__main__":
    main()
