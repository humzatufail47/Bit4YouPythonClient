from typing import List
import json

class Ask:
    quantity: str
    rate: str
    i: int

    def __init__(self, quantity: str, rate: str, i: int) -> None:
        self.quantity = quantity
        self.rate = rate
        self.i = i

class Bid:
    quantity: str
    rate: str
    i: int

    def __init__(self, quantity: str, rate: str, i: int) -> None:
        self.quantity = quantity
        self.rate = rate
        self.i = i


class MarketOrderBookResponse:
    ask: List[Ask]
    bid: List[Bid]

    def __init__(self, ask: List[Ask], bid: List[Bid]) -> None:
        self.ask = ask
        self.bid = bid

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    @staticmethod
    def create_from_json(data):
        json_dictionary = json.loads(data)
        askList = []
        bidList=[]
        for key,values in json_dictionary.items():
            if key =='ask':
                for val in values:
                    askList.append(Ask(**val))
            if key=='bid':
                for val in values:
                    askList.append(Bid(**val))

        return MarketOrderBookResponse(askList,bidList)
