import json


class OrderListRequest:
    page: int
    limit: int
    market: str
    simulation: bool

    def __init__(self, page: int, limit: int, market: str, simulation: bool) -> None:
        self.page = page
        self.limit = limit
        self.market = market
        self.simulation = simulation

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
