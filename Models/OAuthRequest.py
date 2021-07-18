import json


class OAuthRequest:
    grant_type: str
    scope: str
    username: str
    password: str

    def __init__(self, grant_type: str, scope: str, username: str, password: str) -> None:
        self.grant_type = grant_type
        self.scope = scope
        self.username = username
        self.password = password

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True)

    
