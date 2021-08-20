import json


class PortfolioOpenOrderResponse:
    id: int
    type: str
    execute_at: str
    remaining_quantity: str
    remaining_iso: str
    isOpening: int
    market: str
    baseCurrency: str
    invested: str
    quantity: str
    open_time: int
    close_time: None

    def __init__(self, id: int, type: str, execute_at: str, remaining_quantity: str, remaining_iso: str, isOpening: int, market: str, baseCurrency: str, invested: str, quantity: str, open_time: int, close_time: None) -> None:
        self.id = id
        self.type = type
        self.execute_at = execute_at
        self.remaining_quantity = remaining_quantity
        self.remaining_iso = remaining_iso
        self.isOpening = isOpening
        self.market = market
        self.baseCurrency = baseCurrency
        self.invested = invested
        self.quantity = quantity
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
            responselist.append(PortfolioOpenOrderResponse(**resp))
        return responselist
