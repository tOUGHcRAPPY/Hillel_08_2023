# from typing import Any


class PaymentSystem:
    def __init__(self) -> None:
        self.atm_connection: bool = False
        self.__deposit = 0

    # getter
    @property
    def deposit(self):
        return self.__deposit

    # setter
    @deposit.setter
    def deposit(self, amount: int):
        self.__deposit += amount

    # deleter
    @deposit.deleter
    def deposit(self):
        return "Can not delete the object."


paypall = PaymentSystem()
print(paypall.deposit)
paypall.deposit = 12345
paypall.deposit = 12345

print(paypall.deposit)

del paypall.deposit
