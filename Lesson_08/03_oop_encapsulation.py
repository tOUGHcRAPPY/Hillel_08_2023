from typing import Any

methods_blacklist = ["_connect_to_atm", "_cash_counting", "cash_to_client"]


class PaymentSystem:
    def __init__(self) -> None:
        self.atm_connection: bool = False

    def __getattribute__(self, __name: str) -> Any:
        print(f"Accessing to attribute: {__name}")

        if __name in methods_blacklist:
            raise Exception(f"This attribute {__name} is private.")

        return super().__getattribute__(__name)

    def deposit(self, amount: int):
        pass

    def withdraw(self, amount: int):
        self._connect_to_atm()
        self._cash_counting(amount)
        self._cash_to_client(amount)

    def _connect_to_atm(self):
        print("Connection created...")
        self.atm_connection = True

    def _cash_counting(self, amount: int):
        print(f"Total amount of money: {amount}")

    def _cash_to_client(self, amount: int):
        # if self.atm_connection == False:
        #     raise Exception(
        #         f"Access denied. Connection status: {self.atm_connection}"
        #     )
        print("Client gets his withdrawal...")
        print(f"Take your money: {amount}. Don't leave the card...")


paypall = PaymentSystem()
# paypall.deposit(amount=1000)
paypall.withdraw(amount=350)
# paypall.cash_to_client(amount=100)
# paypall._PaymentSystem__cash_to_client(100)
# paypall._connect_to_atm()
