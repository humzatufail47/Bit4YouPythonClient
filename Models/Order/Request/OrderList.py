import json


class OrderListRequest:
    page: int
    limit: int
    market: str
    simulation: bool
    clientId: str
    timingForce: str

    def __init__(self, page: int, limit: int, market: str, simulation: bool, clientId: str, timingForce: str) -> None:
        self.page = page
        self.limit = limit
        self.market = market
        self.simulation = simulation
        self.clientId = clientId
        self.timingForce = timingForce

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
