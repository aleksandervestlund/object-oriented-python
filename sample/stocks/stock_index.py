from stock import Stock


class StockIndex:
    def __init__(self, name: str, stocks: list[Stock]) -> None:
        self.name = name
        self.stocks: list[Stock] = []

        for stock in stocks:
            self.add_stock(stock)

    def stock_price_changed(
        self, stock: Stock, old_value: float, new_value: float
    ) -> None:
        print(
            f"Stock {stock.ticker} price changed from {old_value} to "
            f"{new_value}"
        )

    def add_stock(self, stock: Stock) -> None:
        if stock not in self.stocks:
            stock.add_stock_listener(self)
            self.stocks.append(stock)

    def remove_stock(self, stock: Stock) -> None:
        if stock in self.stocks:
            self.stocks.remove(stock)
            stock.remove_stock_listener(self)

    def get_index(self) -> float:
        return sum(stock.price for stock in self.stocks)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
