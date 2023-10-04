from typing import Any


class User:
    def __init__(self, username: str, password: str):
        self.username: str = username
        self._password: str = password
        self._authorized: bool = False

    def __getattribute__(self, name: str) -> Any:
        if name == "password":
            return "Access denied."
        return super().__getattribute__(name)

    def login(self, username: str, password: str) -> None:
        if self.username == username and self._password == password:
            self._authorized = True
        else:
            self._authorized = False

    @property
    def is_authorized(self) -> bool:
        return self._authorized

    @property
    def password(self):
        return "*****"


user_John = User(username="John", password="qwerty1")


def login(username: str, password: str):
    user_John.login(username, password)
    if user_John.is_authorized:
        print("Access approved.")
    else:
        print("Access denied.")


login("John", "qwerty1")
