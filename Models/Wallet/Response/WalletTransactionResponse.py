from enum import Enum
from typing import Union, List
import json


class FeeAsset(Enum):
    BTC = "BTC"
    USDT = "USDT"


class Market(Enum):
    BTC = "BTC"
    ZIL = "ZIL"


class PaidAsset(Enum):
    USDT = "USDT"
    ZIL = "ZIL"


class Meta:
    pending: bool
    paid_value: Union[float, str]
    paid_asset: PaidAsset
    fee_asset: FeeAsset
    market: Market

    def __init__(self, pending: bool, paid_value: Union[float, str], paid_asset: PaidAsset, fee_asset: FeeAsset, market: Market) -> None:
        self.pending = pending
        self.paid_value = paid_value
        self.paid_asset = paid_asset
        self.fee_asset = fee_asset
        self.market = market


class TypeEnum(Enum):
    ORDER = "order"


class Tx:
    txid: str
    block: None
    confirmations: None
    fee: str
    time: int
    quantity: str
    type: TypeEnum
    meta: Meta

    def __init__(self, txid: str, block: None, confirmations: None, fee: str, time: int, quantity: str, type: TypeEnum, meta: Meta) -> None:
        self.txid = txid
        self.block = block
        self.confirmations = confirmations
        self.fee = fee
        self.time = time
        self.quantity = quantity
        self.type = type
        self.meta = meta


class WalletTransactionResponse:
    balance: str
    pages: int
    txs: List[Tx]

    def __init__(self, balance: str, pages: int, txs: List[Tx]) -> None:
        self.balance = balance
        self.pages = pages
        self.txs = txs

    @staticmethod
    def create_from_json(data):
        json_dictionary = json.loads(data)
        tsx = []
        for resp in json_dictionary.get('txs'):
            tsx.append(Tx(**resp))
        return WalletTransactionResponse(json_dictionary.get('balance'), json_dictionary.get('pages'), tsx)
