from typing import Protocol

from sample.stocks.stock import Stock


class StockListener(Protocol):
    def stock_price_changed(
        self, stock: Stock, old_value: float, new_value: float
    ) -> None:
        ...


def main() -> None:
    pass


if __name__ == "__main__":
    main()
