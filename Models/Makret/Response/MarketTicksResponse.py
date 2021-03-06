import json
class MarketTicksResponse:
    time: int
    open: str
    close: str
    low: str
    high: str
    volume: str
    marketVolume: str

    def __init__(self, time: int, open: str, close: str, low: str, high: str, volume: str, marketVolume: str) -> None:
        self.time = time
        self.open = open
        self.close = close
        self.low = low
        self.high = high
        self.volume = volume
        self.marketVolume = marketVolume
    
    @staticmethod
    def create_from_json(data):
        json_dictionary = json.loads(data)
        responselist = []
        for resp in json_dictionary:
            responselist.append(MarketTicksResponse(**resp))
        return responselist
