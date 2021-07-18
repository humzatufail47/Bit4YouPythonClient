import json


class CancelPortfolioResponse:
    status: str
    message: str

    def __init__(self, status: str, message: str) -> None:
        self.status = status
        self.message = message

    @staticmethod
    def create_from_json(data):
        json_dictionary = json.loads(data)
        return CancelPortfolioResponse(**json_dictionary)
