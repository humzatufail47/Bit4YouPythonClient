import json


class OrderCancel:
    txid: str
    simulation: bool

    def __init__(self, txid: str, simulation: bool) -> None:
        self.txid = txid
        self.simulation = simulation

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
