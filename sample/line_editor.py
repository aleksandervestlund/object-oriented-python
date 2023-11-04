class LineEditor:
    def __init__(self) -> None:
        self._text = ""
        self._insertion_index = 0

    @property
    def insertion_index(self) -> int:
        return self._insertion_index

    @insertion_index.setter
    def insertion_index(self, insertion_index: int) -> None:
        if not 0 <= insertion_index <= len(self._text):
            raise ValueError(
                "Insertion index must be positive, and smaller or equal to "
                "length of text."
            )

        self._insertion_index = insertion_index

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, text: str) -> None:
        self._text = text
        self._insertion_index = len(self._text)

    def left(self) -> None:
        self._insertion_index -= 1
        self._insertion_index = max(self._insertion_index, 0)

    def right(self) -> None:
        self._insertion_index += 1
        self._insertion_index = min(self._insertion_index, len(self._text))

    def insert_string(self, string: str) -> None:
        self._text = (
            f"{self._text[: self._insertion_index]}{string}"
            f"{self._text[self._insertion_index :]}"
        )
        self._insertion_index += len(string)

    def delete_left(self) -> None:
        if self._insertion_index == 0:
            return
        self._text = (
            f"{self._text[: self._insertion_index - 1]}"
            f"{self._text[self._insertion_index :]}"
        )
        self.left()

    def delete_right(self) -> None:
        if self._insertion_index == len(self._text):
            return
        self._text = (
            f"{self._text[: self._insertion_index]}"
            f"{self._text[self._insertion_index + 1 :]}"
        )

    def __repr__(self) -> str:
        return (
            f"{self._text[: self._insertion_index]}|"
            f"{self._text[self._insertion_index :]}"
        )


def main() -> None:
    line_editor = LineEditor()
    print(line_editor)
    line_editor.insert_string("Hei")
    line_editor.left()
    print(line_editor)
    line_editor.delete_right()
    print(line_editor)
    line_editor.insert_string("allo")
    print(line_editor)


if __name__ == "__main__":
    main()
