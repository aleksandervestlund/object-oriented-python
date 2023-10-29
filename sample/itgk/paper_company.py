class PaperCompany:
    def __init__(
        self, paper: int, machines: int, salesmen: int, money: int
    ) -> None:
        self.paper = paper
        self.machines = machines
        self.salesmen = salesmen
        self.money = money

        self.paper_price = 10
        self.machine_price = 100
        self.recruitment_price = 50

    def make_paper(self) -> None:
        self.paper += self.machines

    def sell_paper(self) -> None:
        amount = min(self.paper, self.salesmen)
        self.paper -= amount
        self.money += amount * self.paper_price

    def buy_machines(self, amount: int) -> None:
        price = self.machine_price * amount
        if self.money < price:
            print("Not enough money.")
            return

        self.money -= price
        self.machines += amount

    def recruit_salesmen(self, amount: int) -> None:
        price = self.recruitment_price * amount
        if self.money < price:
            print("Not enough money.")
            return

        self.money -= price
        self.salesmen += amount


def main() -> None:
    comp = PaperCompany(10, 2, 10, 1000)
    comp.sell_paper()
    print(comp.money)  # skal være 1100
    comp.buy_machines(5)
    print(comp.machines)  # skal være 7
    comp.recruit_salesmen(6)
    print(comp.salesmen)  # skal være 16
    comp.make_paper()
    comp.sell_paper()
    print(comp.money)  # skal være 370
    comp.buy_machines(1000)  # skal gi en feilmelding printet ut
    print(comp.money)  # skal fortsatt være 370


if __name__ == "__main__":
    main()
