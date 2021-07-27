import json


class Simulation:
    simulation: bool
    clientId: str
    timingForce: str

    def __init__(self, simulation: bool, clientId: str, timingForce: str) -> None:
        self.simulation = simulation
        self.clientId = clientId
        self.timingForce = timingForce

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
