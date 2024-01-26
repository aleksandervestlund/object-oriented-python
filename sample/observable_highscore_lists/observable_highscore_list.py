from sample.observable_highscore_lists.observable_list import ObservableList


class ObservableHighscoreList(ObservableList):
    def __init__(self, max_size: int) -> None:
        super().__init__()
        self.max_size = max_size

    def accepts_element(self, element: object) -> bool:
        return isinstance(element, int)

    def add_element(self, idx: int, element: object) -> None:
        super().add_element(idx, element)
        self.elements.sort(reverse=True)  # type: ignore
        self.elements = self.elements[: self.max_size]


def main() -> None:
    pass


if __name__ == "__main__":
    main()
