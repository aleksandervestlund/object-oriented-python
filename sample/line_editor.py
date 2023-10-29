class LineEditor:
    def __init__(self, text: str, insertion_index: int) -> None:
        self.text = text
        self.insertion_index = insertion_index

    @property
    def insertion_index(self) -> int:
        return self._insertion_index

    @insertion_index.setter
    def insertion_index(self, insertion_index: int) -> None:
        if not 0 <= insertion_index <= len(self.text):
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
        self.insertion_index = len(self._text)

    def left(self, n: int) -> None:
        self.insertion_index -= n
        if self.insertion_index < 0:
            self.insertion_index = len(self.text)

    def right(self, n: int) -> None:
        self.insertion_index += n
        if self.insertion_index > 0:
            self.insertion_index = len(self.text)

    def insert_string(self, string: str) -> None:
        self._text = (
            f"{self.text[: self.insertion_index]}{string}"
            f"{self.text[self.insertion_index :]}"
        )
        self.right(n=len(string))

    def delete_left(self) -> None:
        if self.insertion_index == 0:
            return
        self._text = (
            f"{self.text[: self.insertion_index - 1]}"
            f"{self.text[self.insertion_index :]}"
        )
        self.left(n=1)

    def delete_right(self) -> None:
        if self.insertion_index == len(self.text):
            return
        self._text = (
            f"{self.text[: self.insertion_index]}"
            f"{self.text[self.insertion_index + 1 :]}"
        )

    def __repr__(self) -> str:
        return (
            f"{self.text[: self.insertion_index]}|"
            f"{self.text[self.insertion_index :]}"
        )


def main() -> None:
    line_editor = LineEditor("Hei", 3)
    print(line_editor)
    line_editor.left(2)
    print(line_editor)
    line_editor.delete_right()
    print(line_editor)
    line_editor.insert_string("allo")
    print(line_editor)


if __name__ == "__main__":
    main()
