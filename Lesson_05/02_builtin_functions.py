from pprint import pprint as print

# print("John")
# print(repr("John"))


class Person:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"I am class Person print for {self.name}"

    def __repr__(self) -> str:
        return f"I am class Person representation for {self.name}"


# john = Person(name="John")

# print(john)
# print(repr(john))

# contact_info_existence = (
#     True,
#     True,
#     False,
#     True
# )

# print(contact_info_existence)

# for item in contact_info_existence:
#     if item is False:
#         print("Some info is missing.")
#         break


# if not all(contact_info_existence):
#     print("Some info is missing.")

# if any(contact_info_existence):
#     print("At least some info has been collected.")


# team = ["Jack", "Rosa", "Mike", "Alice", "Dafna", "Luke", "John"]
# print(team)
# print(sorted(team))

# print(ord("V"))
# print(chr(86))

team: list[dict] = [
    {"name": "John", "age": 15, "number": 12},
    {"name": "Jenny", "age": 14, "number": 10},
    {"name": "Mike", "age": 14, "number": 7},
    {"name": "Lisa", "age": 15, "number": 15},
    {"name": "Jack", "age": 14, "number": 9},
]


def sort_by_age(item: dict):
    return item["age"]


print(team)
print("Sorted")
print(sorted(team, key=sort_by_age))
print(id(team))
print(isinstance(team, list))
print(hash("John"))

lambda argument1, argument2: argument1 + argument2
