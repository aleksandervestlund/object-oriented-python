class CookieFactory:
    def __init__(self, money: int) -> None:
        self.money = money
        self.machine_active = False
        self.cookies = 0

    def start_machine(self) -> None:
        self.machine_active = True

    def stop_machine(self) -> None:
        self.machine_active = False

    def make_cookies(self, amount: int) -> None:
        if self.machine_active:
            self.cookies += amount
        else:
            print("Can't make cookies with an inactive machine.")

    def sell_cookies(self, amount: int) -> None:
        if self.cookies < amount:
            print("Too few cookies available.")
            return

        self.money += 5 * amount
        self.cookies -= amount
