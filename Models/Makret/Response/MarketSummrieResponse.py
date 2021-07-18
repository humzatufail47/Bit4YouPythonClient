import json


class MarketSummrieResponse:
    market: str
    marketCap: str
    supply: str
    open: str
    high: str
    low: str
    last: str
    prevDay: str
    volume: str
    bid: str
    ask: str

    def __init__(self, market: str, marketCap: str, supply: str, open: str, high: str, low: str, last: str, prevDay: str, volume: str, bid: str, ask: str) -> None:
        self.market = market
        self.marketCap = marketCap
        self.supply = supply
        self.open = open
        self.high = high
        self.low = low
        self.last = last
        self.prevDay = prevDay
        self.volume = volume
        self.bid = bid
        self.ask = ask

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    @staticmethod
    def create_from_json(data):
        json_dictionary = json.loads(data)
        responselist = []
        for resp in json_dictionary:
            responselist.append(MarketSummrieResponse(**resp))
        return responselist
