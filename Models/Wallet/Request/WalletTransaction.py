import json


class WalletTransaction:
    iso: str
    simulation: bool
    clientId: str
    timingForce: str

    def __init__(self, iso: str, simulation: bool, clientId: str, timingForce: str) -> None:
        self.iso = iso
        self.simulation = simulation
        self.clientId = clientId
        self.timingForce = timingForce

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
