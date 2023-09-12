from functools import wraps

class Printer:
	def __init__(self, name: str, ip: str, port: int) -> None:
		self.name: str = name
		self.ip: str = ip
		self.port: int = port
	def __str__(self) -> str:
		return f"{self.name}@{self.ip}:{self.port}"
	

hp_black = Printer(name="HP Black", ip="11.12.13.14", port=12345)
hp_white = Printer(name="HP White", ip="12.13.14.15", port=23456)
	

def open_connection(printer: Printer):
	print("Checking drivers...")
	print(f"Connection to {printer}")


def use_printer(printer: Printer, text: str):
	print(f"Printing the text: {text}")


def close_connection(printer: Printer):
	print(f"Connection with {printer} closed.")


def printer_workflow(func):
	def wrapper(printer: Printer, document: str):
		open_connection(printer)
		func(printer, document)
		close_connection(printer)
	return wrapper

@printer_workflow
def use_printer(printer: Printer, document: str):
	print(f"Printing the text: {document}")


def printer_workflow_connection(printer: Printer):
	def outter(func):
		@wraps(func)
		def inner(document: str):
			open_connection(printer)
			func(document)
			close_connection(printer)
		return inner
	return outter

@printer_workflow_connection(printer=hp_black)
def print_document(document: str):
	print(f"Printing document...: {document}")




# open_connection(printer=hp_black)
# use_printer(printer=hp_black, text="Hello, World!")
# close_connection(printer=hp_black)
use_printer(printer=hp_white, document="I am white.")
print_document("Simle text.")