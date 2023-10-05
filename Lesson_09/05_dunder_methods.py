import random
import string


class Team:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self._team: dict = {"John": {}, "Marry": {}, "Sarah": {}}

    def __getitem__(self, key: str):
        if key not in self._team.keys():
            print(f"There is no such player as {key} in team.")
        else:
            # print(f"{self._team[key]}")
            return f"{self._team[key]}."


team_Monkeys = Team(name="Monkeys")
print(team_Monkeys["John"])
print(team_Monkeys["Loyd"])


class User:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password


class UsersFactory:
    def __init__(self, *args) -> None:
        self._names = list(args)
        self._init_users

    @property
    def random_password(self):
        return "".join(
            [random.choice(string.ascii_letters) for i in range(10)]
        )

    def _init_users(self):
        self._users = [
            User(username=self.username, password=self.random_password)
            for names in self._names
        ]

    def __getitem__(self, key: str):
        if key not in self._data.keys():
            print(f"There is no such player as {key} in team.")
        else:
            # print(f"{self._team[key]}")
            return f"{self._data[key]}."


team_DataDay = UsersFactory("John", "Marry", "Mark")
