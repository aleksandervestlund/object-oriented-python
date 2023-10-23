from typing import Self


class Partner:
    def __init__(self, name: str) -> None:
        self.name = name
        self.partner: (Self | None) = None

    def __repr__(self) -> str:
        return self.name

    def set_partner(self, partner: (Self | None)) -> None:
        if not partner:
            if self.partner:
                self.partner.partner = None
        else:
            partner.set_partner(None)
            self.set_partner(None)
            partner.partner = self

        self.partner = partner


def main() -> None:
    p1 = Partner("Ola")
    p2 = Partner("Astrid")
    p3 = Partner("Per")
    p4 = Partner("Ingrid")

    p1.set_partner(p2)
    assert p1.partner is p2
    assert p2.partner is p1

    p1.set_partner(None)
    assert p1.partner is None
    assert p2.partner is None

    p1.set_partner(p2)
    p3.set_partner(p4)
    p1.set_partner(p4)
    assert p1.partner is p4
    assert p4.partner is p1
    assert p2.partner is None
    assert p3.partner is None


if __name__ == "__main__":
    main()
