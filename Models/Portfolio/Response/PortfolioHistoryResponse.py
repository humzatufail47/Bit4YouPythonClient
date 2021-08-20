from enum import Enum
import json


class BaseCurrency(Enum):
    USDT = "USDT"


class Market(Enum):
    BCH = "BCH"
    BTC = "BTC"
    EOS = "EOS"


class PortfolioHistoryResponse:
    id: int
    market: Market
    baseCurrency: BaseCurrency
    invested: str
    closed_amount: str
    quantity: str
    fee: str
    open_time: int
    close_time: int

    def __init__(self, id: int, market: Market, baseCurrency: BaseCurrency, invested: str, closed_amount: str, quantity: str, fee: str, open_time: int, close_time: int) -> None:
        self.id = id
        self.market = market
        self.baseCurrency = baseCurrency
        self.invested = invested
        self.closed_amount = closed_amount
        self.quantity = quantity
        self.fee = fee
        self.open_time = open_time
        self.close_time = close_time

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    @staticmethod
    def create_from_json(data):
        json_dictionary = json.loads(data)
        responselist = []
        for resp in json_dictionary:
            responselist.append(PortfolioHistoryResponse(**resp))
        return responselist
