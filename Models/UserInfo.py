from datetime import datetime
import json


class UserInfo:
    sub: int
    iss: str
    aud: str
    iat: int
    auth_time: int
    verified: bool
    is_child: bool
    full_locked: bool
    name: str
    family_name: str
    given_name: str
    middle_name: str
    gender: str
    birthdate: datetime
    birthplace: str
    zoneinfo: str
    locale: str
    currency: str
    updated_at: datetime
    id_number: str
    id_expiration: str
    nationality: str

    def __init__(self, sub: int, iss: str, aud: str, iat: int, auth_time: int, verified: bool, is_child: bool, full_locked: bool, name: str, family_name: str, given_name: str, middle_name: str, gender: str, birthdate: datetime, birthplace: str, zoneinfo: str, locale: str, currency: str, updated_at: datetime, id_number: str, id_expiration: str, nationality: str) -> None:
        self.sub = sub
        self.iss = iss
        self.aud = aud
        self.iat = iat
        self.auth_time = auth_time
        self.verified = verified
        self.is_child = is_child
        self.full_locked = full_locked
        self.name = name
        self.family_name = family_name
        self.given_name = given_name
        self.middle_name = middle_name
        self.gender = gender
        self.birthdate = birthdate
        self.birthplace = birthplace
        self.zoneinfo = zoneinfo
        self.locale = locale
        self.currency = currency
        self.updated_at = updated_at
        self.id_number = id_number
        self.id_expiration = id_expiration
        self.nationality = nationality

    @staticmethod
    def create_from_json(data):
        json_dictionary = json.loads(data)
        return UserInfo(**json_dictionary)
