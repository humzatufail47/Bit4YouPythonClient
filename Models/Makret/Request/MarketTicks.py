import json


class MarketTicks:
    market: str
    interval: int

    def __init__(self, market: str, interval: int) -> None:
        self.market = market
        self.interval = interval

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
