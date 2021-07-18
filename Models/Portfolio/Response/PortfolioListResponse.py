from typing import List
import json


class Item:
    id: int
    base_iso: str
    market: str
    invested: str
    quantity: str
    open_time: int

    def __init__(self, id: int, base_iso: str, market: str, invested: str, quantity: str, open_time: int) -> None:
        self.id = id
        self.base_iso = base_iso
        self.market = market
        self.invested = invested
        self.quantity = quantity
        self.open_time = open_time


class PortfolioListResponse:
    items: List[Item]
    wallet: str

    def __init__(self, items: List[Item], wallet: str) -> None:
        self.items = items
        self.wallet = wallet
    
    @staticmethod
    def create_from_json(data):
        json_dictionary = json.loads(data)
        return PortfolioListResponse(**json_dictionary)
