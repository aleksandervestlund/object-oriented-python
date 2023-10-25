from typing import Protocol

from highscore_list import HighscoreList


class HighscoreListListener(Protocol):
    def list_changed(self, highscore_list: HighscoreList, idx: int) -> None:
        ...
