from typing import TypedDict

import requests


class User(TypedDict):
    name: str
    roles: list[str]


class NotAuthorizedException(Exception):
    pass


class Database:
    @classmethod
    def get_user(cls, username, password) -> User:
        msg = "Could not connect to database"
        raise requests.exceptions.ConnectionError(msg)


def validate_roles(required_roles: list[str], user_roles: list[str]) -> bool:
    for role in required_roles:
        if role not in user_roles:
            raise NotAuthorizedException
    return True


def authorize_user(
    database: Database, username: str, password: str, required_roles: list[str],
) -> User:
    user = database.get_user(username, password)
    validate_roles(required_roles, user["roles"])
    return user
