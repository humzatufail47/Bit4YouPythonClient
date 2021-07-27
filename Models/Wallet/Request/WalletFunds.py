import json


class WalletFunds:
    iso: str
    quantity: float
    address: str
    clientId: str
    timingForce: str

    def __init__(self, iso: str, quantity: float, address: str, clientId: str, timingForce: str) -> None:
        self.iso = iso
        self.quantity = quantity
        self.address = address
        self.clientId = clientId
        self.timingForce = timingForce


    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
