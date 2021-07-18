import json


class Fee:
    quantity: str
    iso: str

    def __init__(self, quantity: str, iso: str) -> None:
        self.quantity = quantity
        self.iso = iso


class Position:
    id: None
    history_id: None

    def __init__(self, id: None, history_id: None) -> None:
        self.id = id
        self.history_id = history_id


class OrderPendingResponse:
    txid: str
    type: str
    market: str
    isOpen: bool
    requested_rate: str
    quantity: str
    base_quantity: str
    blocked_quantity: str
    remaining: Fee
    fee: Fee
    position: Position
    open_time: int
    update_time: int

    def __init__(self, txid: str, type: str, market: str, isOpen: bool, requested_rate: str, quantity: str, base_quantity: str, blocked_quantity: str, remaining: Fee, fee: Fee, position: Position, open_time: int, update_time: int) -> None:
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

    @staticmethod
    def create_from_json(data):
        json_dictionary = json.loads(data)
        responselist = []
        for resp in json_dictionary:
            responselist.append(OrderPendingResponse(**resp))
        return responselist
