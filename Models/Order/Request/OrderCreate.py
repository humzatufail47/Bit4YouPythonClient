import json


class CreateOrder:
    market: str
    type: int
    quantity: int
    quantity_iso: None
    rate: float
    simulation: bool

    def __init__(self, market: str, type: int, quantity: int, quantity_iso: None, rate: float, simulation: bool) -> None:
        self.market = market
        self.type = type
        self.quantity = quantity
        self.quantity_iso = quantity_iso
        self.rate = rate
        self.simulation = simulation

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
