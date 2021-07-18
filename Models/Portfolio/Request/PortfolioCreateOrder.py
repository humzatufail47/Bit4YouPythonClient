import json


class PortfolioCreateOrder:
    market: str
    quantity: float
    rate: float
    simulation: bool

    def __init__(self, market: str, quantity: float, rate: float, simulation: bool) -> None:
        self.market = market
        self.quantity = quantity
        self.rate = rate
        self.simulation = simulation

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
