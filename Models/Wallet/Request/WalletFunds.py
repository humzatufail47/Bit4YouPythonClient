import json


class WalletFunds:
    iso: str
    quantity: float
    address: str

    def __init__(self, iso: str, quantity: float, address: str) -> None:
        self.iso = iso
        self.quantity = quantity
        self.address = address

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
