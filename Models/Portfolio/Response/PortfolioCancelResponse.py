import json


class CancelPortfolioResponse:
    status: str
    message: str

    def __init__(self, status: str, message: str) -> None:
        self.status = status
        self.message = message

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    @staticmethod
    def create_from_json(data):
        json_dictionary = json.loads(data)
        return CancelPortfolioResponse(**json_dictionary)
