from typing import Optional
import json


class Ath:
    time: int
    value: str

    def __init__(self, time: int, value: str) -> None:
        self.time = time
        self.value = value

    @staticmethod
    def create_from_json(data):
        json_dictionary = json.loads(data)
        return Ath(**json_dictionary)


class MarketListResponse:
    iso: str
    name: str
    precision: int
    value: str
    change: str
    spread: str
    supply: str
    ath: Optional[Ath]

    def __init__(self, iso: str, name: str, precision: int, value: str, change: str, spread: str, supply: str, ath: Optional[Ath]=None) -> None:
        self.iso = iso
        self.name = name
        self.precision = precision
        self.value = value
        self.change = change
        self.spread = spread
        self.supply = supply
        self.ath = ath

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)



    @staticmethod
    def create_from_json(data):
        json_dictionary = json.loads(data)
        responselist = []
        for resp in json_dictionary:
            responselist.append(MarketListResponse(**resp))
        return responselist
