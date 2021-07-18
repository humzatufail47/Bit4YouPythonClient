import json


class MarketOrderBook:
    market: str
    limit: int
    state: bool

    def __init__(self, market: str, limit: int, state: bool) -> None:
        self.market = market
        self.limit = limit
        self.state = state

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
