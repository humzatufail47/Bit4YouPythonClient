import json


class MarketOrderBook:
    market: str
    limit: int
    state: bool
    clientId: str
    timingForce: str

    def __init__(self, market: str, limit: int, state: bool,clientId: str, timingForce: str) -> None:
        self.market = market
        self.limit = limit
        self.state = state
        self.clientId = clientId
        self.timingForce = timingForce

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
