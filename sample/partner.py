from __future__ import annotations


class Partner:
    def __init__(self, name: str) -> None:
        self.name = name
        self.partner: Partner | None = None

    def __repr__(self) -> str:
        return self.name

    def set_partner(self, partner: Partner | None) -> None:
        if partner is self:
            raise ValueError("Cannot partner with self")

        if partner is None:
            if self.partner is not None:
                self.partner.partner = None
        else:
            partner.set_partner(None)
            self.set_partner(None)
            partner.partner = self

        self.partner = partner


def main() -> None:
    pass


if __name__ == "__main__":
    main()
