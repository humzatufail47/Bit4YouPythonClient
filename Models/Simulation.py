import json


class Simulation:
    simulation: bool

    def __init__(self, simulation: bool) -> None:
        self.simulation = simulation

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
