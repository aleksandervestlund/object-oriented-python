from __future__ import annotations
from stock_listener import StockListener


class Stock:
    def __init__(self, ticker: str, price: float) -> None:
        self.ticker = ticker
        self.price = price

        self.listeners: list[StockListener] = []

    def set_price(self, price: float) -> None:
        if price <= 0.0:
            raise ValueError("Price must be positive")

        old_price = self.price
        self.price = price

        for listener in self.listeners:
            listener.stock_price_changed(self, old_price, self.price)

    def add_stock_listener(self, listener: StockListener) -> None:
        if listener not in self.listeners:
            self.listeners.append(listener)

    def remove_stock_listener(self, listener: StockListener) -> None:
        if listener in self.listeners:
            self.listeners.remove(listener)

    def stock_price_changed(
        self, stock: Stock, old_value: float, new_value: float
    ) -> None:
        for listener in self.listeners:
            listener.stock_price_changed(stock, old_value, new_value)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
