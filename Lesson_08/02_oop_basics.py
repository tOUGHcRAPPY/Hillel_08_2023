class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    def __str__(self) -> str:
        return f"Class object name is {self.name}"

    def __repr__(self) -> str:
        return f"{self.name=}, {self.age=}"

    def get_name(self):
        print(f"Person's name is: {self.name}")
        return f"Person's name is: {self.name}"


person_John = Person(name="John", age=11)
person_Marry = Person(name="Marry", age=13)

print(f"{person_John.get_name()}, {person_Marry.get_name()}")
person_John.get_name()
person_Marry.get_name()
print("------------")
print(person_John)
print(person_Marry)

print(person_John.name)

team = [
    {"name": "John", "age": 13},
    {"name": "Marry", "age": 14},
]

print(team[1]["name"])

print(person_John.__dict__)
person_John.name = "Michael"
person_John.age = 12
print(person_John.__dict__)

team_1 = [{"name": "Alex", "age": 15}, {"name": "Fiona", "age": 14}]
team_2 = [{"name": "Mike", "age": 13}, {"name": "Caroline", "age": 12}]
comb_team = team_1 + team_2

print(comb_team)

for item in comb_team:
    print(item.get("name"))
