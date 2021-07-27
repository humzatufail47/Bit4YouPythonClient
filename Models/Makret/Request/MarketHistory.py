import json


class MarketHistory:
    market: str
    limit: int
    welcome2_from: str
    to: str
    clientId: str
    timingForce: str

    def __init__(self, market: str, limit: int, welcome2_from: str, to: str, clientId: str, timingForce: str) -> None:
        self.clientId = clientId
        self.timingForce = timingForce
        self.market = market
        self.limit = limit
        self.welcome2_from = welcome2_from
        self.to = to

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
