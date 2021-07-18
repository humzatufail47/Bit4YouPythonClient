import json


class ClosePortfolioPosition:
    id: int
    simulation: bool

    def __init__(self, id: int, simulation: bool) -> None:
        self.id = id
        self.simulation = simulation

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
