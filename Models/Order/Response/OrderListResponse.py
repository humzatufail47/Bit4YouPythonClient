from enum import Enum
from typing import Optional, Union
import json


class ISO(Enum):
    BTC = "BTC"
    USDT = "USDT"


class Fee:
    quantity: str
    iso: ISO

    def __init__(self, quantity: str, iso: ISO) -> None:
        self.quantity = quantity
        self.iso = iso


class Market(Enum):
    USDT_BTC = "USDT-BTC"


class Position:
    id: Optional[int]
    history_id: None

    def __init__(self, id: Optional[int], history_id: None) -> None:
        self.id = id
        self.history_id = history_id


class Remaining:
    quantity: Union[int, str]
    iso: ISO

    def __init__(self, quantity: Union[int, str], iso: ISO) -> None:
        self.quantity = quantity
        self.iso = iso


class TypeEnum(Enum):
    BUY = "buy"
    SELL = "sell"


class OrderListResponse:
    txid: str
    type: TypeEnum
    market: Market
    isOpen: bool
    requested_rate: Optional[str]
    quantity: str
    base_quantity: str
    blocked_quantity: Union[int, str]
    remaining: Remaining
    fee: Fee
    position: Position
    open_time: int
    update_time: int

    def __init__(self, txid: str, type: TypeEnum, market: Market, isOpen: bool, requested_rate: Optional[str], quantity: str, base_quantity: str, blocked_quantity: Union[int, str], remaining: Remaining, fee: Fee, position: Position, open_time: int, update_time: int) -> None:
        self.txid = txid
        self.type = type
        self.market = market
        self.isOpen = isOpen
        self.requested_rate = requested_rate
        self.quantity = quantity
        self.base_quantity = base_quantity
        self.blocked_quantity = blocked_quantity
        self.remaining = remaining
        self.fee = fee
        self.position = position
        self.open_time = open_time
        self.update_time = update_time

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    @staticmethod
    def create_from_json(data):
        json_dictionary = json.loads(data)
        responselist = []
        for resp in json_dictionary:
            responselist.append(OrderListResponse(**resp))
        return responselist
