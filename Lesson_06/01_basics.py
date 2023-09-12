from typing import Callable, Any


def logger(func: Callable, name: str) -> None:
	print(f"Running the {func.__name__}...")
	results: Any = func(name)
	if results:
		print(f"Results: {results}")
	else:
		print("No results...")

def greeting(name: str) -> None:
	print(f"Hey {name}!")


# greeting("John")
# logger(greeting, name="Sarah")


def more_compicated_logger(func: Callable) -> Callable:
	print(f"Running the {func.__name__}...")
	def wrapper(name: str):
		results: Any = func(name)
		if results:
			print(f"Results: {results}")
		else:
			print("No results...")	
	return wrapper

def greeting(name: str) -> None:
	print(f"Hey {name}!")


@more_compicated_logger
def greeting(name: str) -> None:
	print(f"Hey {name}!")

more_compicated_logger(greeting)(name="T-800")