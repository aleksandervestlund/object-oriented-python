from stock import Stock
from stock_listener import StockListener


class SmartStock(Stock):
    def __init__(self, name: str, price: float) -> None:
        super().__init__(name, price)

        self.interval_listeners: dict[StockListener, tuple[float, float]] = {}
        self.difference_listeners: dict[
            StockListener, tuple[float, float]
        ] = {}

    def add_stock_listener_interval(
        self, listener: StockListener, minimum: float, maximum: float
    ) -> None:
        self.interval_listeners[listener] = (minimum, maximum)

    def remove_stock_listener(self, listener: StockListener) -> None:
        if listener in self.interval_listeners:
            del self.interval_listeners[listener]

    def add_stock_listener_difference(
        self, listener: StockListener, difference: float
    ) -> None:
        self.difference_listeners[listener] = (difference, self.price)

    def remove_stock_listener_difference(
        self, listener: StockListener
    ) -> None:
        if listener in self.difference_listeners:
            del self.difference_listeners[listener]

    def stock_price_changed(
        self, stock: Stock, old_value: float, new_value: float
    ) -> None:
        super().stock_price_changed(stock, old_value, new_value)

        for listener, interval in self.interval_listeners.items():
            if interval[0] <= new_value <= interval[1]:
                listener.stock_price_changed(stock, old_value, new_value)

        for listener, elem in self.difference_listeners.items():
            difference, old_value = elem
            if abs(new_value - old_value) >= difference:
                listener.stock_price_changed(stock, old_value, new_value)
                self.difference_listeners[listener] = (difference, new_value)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
