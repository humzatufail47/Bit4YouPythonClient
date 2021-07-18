from typing import Optional, Union
import json


class WalletBalanceResponse:
    iso: str
    name: str
    tx: str
    tx_enabled: Optional[bool]
    erc20: Optional[bool]
    balance: Union[int, str]
    tx_explorer: Optional[str]
    digits: Optional[int]

    def __init__(self, iso: str, name: str, tx: str,balance: Union[int, str],tx_enabled: Optional[bool]=None, erc20: Optional[bool]=None, tx_explorer: Optional[str] = None, digits: Optional[int] = None) -> None:
        self.iso = iso
        self.name = name
        self.tx = tx
        self.tx_enabled = tx_enabled
        self.erc20 = erc20
        self.balance = balance
        self.tx_explorer = tx_explorer
        self.digits = digits

    @staticmethod
    def create_from_json(data):
        json_dictionary = json.loads(data)
        responselist = []
        for resp in json_dictionary:
            responselist.append(WalletBalanceResponse(**resp))
        return responselist
