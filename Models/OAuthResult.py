import json


class OAuthResult:
    access_token: str
    token_type: str
    id_token: str
    expires_in: int
    auth_exp: int

    def __init__(self, access_token: str, token_type: str, id_token: str, expires_in: int, auth_exp: int) -> None:
        self.access_token = access_token
        self.token_type = token_type
        self.id_token = id_token
        self.expires_in = expires_in
        self.auth_exp = auth_exp

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    @staticmethod
    def create_from_json(data):
        json_dictionary = json.loads(data)
        return OAuthResult(**json_dictionary)
