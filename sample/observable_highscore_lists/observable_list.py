from abc import ABC, abstractmethod

from observable_list_listener import ObservableListListener


class ObservableList(ABC):
    def __init__(self) -> None:
        self.listeners: list[ObservableListListener] = []
        self.elements: list[object] = []

    @abstractmethod
    def accepts_element(self, element: object) -> bool:
        pass

    def size(self) -> int:
        return len(self.elements)

    def get_element(self, idx: int) -> object:
        return self.elements[idx]

    def add_element(self, idx: int, element: object) -> None:
        if not self.accepts_element(element):
            raise ValueError("Invalid element")

        self.elements.insert(idx, element)

    def remove_element(self, idx: int) -> None:
        self.elements.pop(idx)

    def add_observable_list_listener(
        self, listener: ObservableListListener
    ) -> None:
        if listener not in self.listeners:
            self.listeners.append(listener)

    def remove_observable_list_listener(
        self, listener: ObservableListListener
    ) -> None:
        if listener in self.listeners:
            self.listeners.remove(listener)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
