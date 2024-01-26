from sample.observable_highscore_lists.observable_highscore_list import (
    ObservableHighscoreList,
)
from sample.observable_highscore_lists.observable_list import ObservableList


class ObservableHighscoreListProgram:
    def __init__(self) -> None:
        self.observable_highscore_list = ObservableHighscoreList(10)
        self.observable_highscore_list.add_observable_list_listener(self)

    def list_changed(self, source: ObservableList, idx: int) -> None:
        print(
            f"List changed at index {idx}. Highscore list is now "
            f"{source.elements}"
        )

    def run(self) -> None:
        print("Enter highscores. Negative value and non-digit input ends")
        while True:
            try:
                value = int(input("Enter value: "))
            except ValueError:
                break
            if value < 0:
                break
            self.observable_highscore_list.add_element(0, value)
        print(
            "Highscore list ended up being: "
            f"{self.observable_highscore_list.elements}"
        )


def main() -> None:
    pass


if __name__ == "__main__":
    main()
