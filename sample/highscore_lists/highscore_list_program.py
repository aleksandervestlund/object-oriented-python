from sample.highscore_lists.highscore_list import HighscoreList


class HighscoreListProgram:
    def __init__(self) -> None:
        self.highscore_list = HighscoreList(10)
        self.highscore_list.add_highscore_list_listener(self)

    def list_changed(self, highscore_list: HighscoreList, idx: int) -> None:
        print(
            f"List changed for at index {idx}, and is now "
            f"{highscore_list.results}."
        )

    def run(self) -> None:
        while True:
            try:
                self.highscore_list.add_result(int(input("Enter result: ")))
            except (KeyboardInterrupt, ValueError):
                break

        print(f"Program terminated. Result was {self.highscore_list.results}.")


def main() -> None:
    highscore_list_program = HighscoreListProgram()
    highscore_list_program.run()


if __name__ == "__main__":
    main()
