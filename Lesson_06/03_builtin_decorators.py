import time
from typing import Callable

class Person:
	def __init__(self, name: str, age: int) -> None:
		self.name: str = name
		self.age: int = age

	def perf_counter(func: callable):
		def inner(*args, **kwargs):
			start = time.perf_counter()
			result = func(*args, **kwargs)
			exec_time = time.perf_counter() - start
			print(f"Exec time of: {func.__name__} is {exec_time}")
			return result
		return inner

	@perf_counter
	def person_greetings(self):
		print(f"{self.name} say's: 'Hello!' to naked ladies!")
		return f"That's message from {self.name}."
	
	@staticmethod
	def person_goodbye(name: str):
		print(f"{name} say's: 'See you tomorrow!'")

	@property
	def is_adult(self) -> bool:
		if self.age < 18:
			return False
		else:
			return True
		




class NotPerson:
	_instance = None
	_initialized: bool = False

	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = super().__new__(cls)

		return cls._instance
	

	def __init__(self, name: str, age: int) -> None:
		if self._initialized:
			return
		
		self.name: str = name
		self.age: int = age

		self._initialized = True

	@classmethod
	def notperson_greetings(cls):
		print(f"{cls._instance} say's: 'Hello to eveyone!'")


person_John = Person(name="John", age=19)

notperson_Marry = NotPerson(name="Marry", age=18)
notperson_Sarah = NotPerson(name="Sarah", age=18)

print(person_John.name)
print(person_John.person_greetings())
print(notperson_Marry.name)
print(notperson_Sarah.name)
# print(NotPerson.__name__)
# print(Person.__name__)
person_John.person_greetings()
notperson_Marry.notperson_greetings()
Person.person_goodbye(name="Mark")
person_John.person_goodbye(name=person_John.name)
print(person_John.is_adult)