import json


class MarketHistoryResponse:
    id: str
    time: int
    quantity: str
    rate: str
    buy: bool

    def __init__(self, id: str, time: int, quantity: str, rate: str, buy: bool) -> None:
        self.id = id
        self.time = time
        self.quantity = quantity
        self.rate = rate
        self.buy = buy

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    @staticmethod
    def create_from_json(data):
        json_dictionary = json.loads(data)
        responselist = []
        for resp in json_dictionary:
            responselist.append(MarketHistoryResponse(**resp))
        return responselist
