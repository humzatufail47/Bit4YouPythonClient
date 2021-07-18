import json


class WalletTransaction:
    iso: str
    simulation: bool

    def __init__(self, iso: str, simulation: bool) -> None:
        self.iso = iso
        self.simulation = simulation

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
