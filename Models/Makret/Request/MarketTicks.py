import json


class MarketTicks:
    market: str
    interval: int
    clientId: str
    timingForce: str

    def __init__(self, market: str, interval: int,clientId: str, timingForce: str) -> None:
        self.market = market
        self.interval = interval
        self.clientId = clientId
        self.timingForce = timingForce

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
