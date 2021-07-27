import json


class PortfolioCreateOrder:
    market: str
    quantity: float
    rate: float
    simulation: bool
    clientId: str
    timingForce: str

    def __init__(self, market: str, quantity: float, rate: float, simulation: bool, clientId: str,
                 timingForce: str) -> None:
        self.market = market
        self.quantity = quantity
        self.rate = rate
        self.simulation = simulation
        self.clientId = clientId
        self.timingForce = timingForce

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
