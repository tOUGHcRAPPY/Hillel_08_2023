import random
import string


class User:
    def __init__(self, username: str, password: str):
        self.username: str = username
        self.password: str = password

    @classmethod
    def create_with_temp_password(cls, username: str):
        temp_chars: list[str] = [
            random.choice(string.ascii_letters) for i in range(16)
        ]
        temp_password = "".join(temp_chars)
        return cls(username=username, password=temp_password)


def create_user_with_temp_password(username: str):
    temp_chars: list[str] = [
        random.choice(string.ascii_letters) for i in range(16)
    ]
    temp_password = "".join(temp_chars)
    return User(username=username, password=temp_password)


user_John = User(username="John", password="abrakadabra88")
user_Marry = create_user_with_temp_password(username="Marry")
user_Chubaka = User.create_with_temp_password(username="Chubaka")

print(user_John.password)
print(user_Marry.password)
print(user_Chubaka.password)
