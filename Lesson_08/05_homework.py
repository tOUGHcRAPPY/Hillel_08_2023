# Acceptance criteria:
# If I create 2 instances of a Price class
# I want to do operations between them:
# add prices with same currency
# do a subtraction of prices with same currency
# *Additional: operations between prices with different currencies:
# If price instances currencies are different I want to do a double conversion
# USD is a middle currency
# If right price is USD the regular conversation (not double) is happening
# If prices currencies is the same conversion is not happening
# Result currency after the operation is a currency of
# the price that is on the left or USD (for your decision)


class Price:
    exchange_rates = {
        ("USD", "EUR"): 1.07,
        ("USD", "GBP"): 1.23,
        ("USD", "MXN"): 0.06,
        ("USD", "AUD"): 0.64,
        ("USD", "CAD"): 0.74,
        ("USD", "UAH"): 0.03,
        ("USD", "PLN"): 0.23,
        ("USD", "CHF"): 1.11,
        ("USD", "RUB"): 0.01,
        ("USD", "CNY"): 0.14,
    }

    def __init__(self, amount: int, currency: str) -> None:
        self.amount: int = amount
        self.currency: str = currency.upper()

    @staticmethod
    def _convert_to_usd_if_needed(func):
        def wrapper(self, other):
            if self.currency != "USD":
                if ("USD", self.currency) in self.exchange_rates:
                    conversion_rate = self.exchange_rates[
                        ("USD", self.currency)
                    ]
                    self.amount *= conversion_rate
                    self.currency = "USD"
                else:
                    raise ValueError(
                        f"Currency conversion from {self.currency} +\
                            to USD is not available."
                    )

            if other.currency != "USD":
                if ("USD", other.currency) in self.exchange_rates:
                    conversion_rate = self.exchange_rates[
                        ("USD", other.currency)
                    ]
                    other.amount *= conversion_rate
                    other.currency = "USD"
                else:
                    raise ValueError(
                        f"Currency conversion from {other.currency} +\
                            to USD is not available."
                    )

            return func(self, other)

        return wrapper

    @_convert_to_usd_if_needed
    def add(self, other):
        result_amount = self.amount + other.amount
        return Price(result_amount, self.currency)

    @_convert_to_usd_if_needed
    def subtract(self, other):
        result_amount = self.amount - other.amount
        return Price(result_amount, self.currency)

    def __str__(self):
        return f"{self.amount} {self.currency}"


price1 = Price(100, "MXN")
price2 = Price(125, "USD")
price3 = Price(100, "RUB")
price4 = Price(2, "USD")

result = price2.add(price4)
print(f"Addition: {result}")

result = price4.subtract(price2)
print(f"Subtraction: {result}")

result = price1.add(price3)
print(f"Addition: {result}")

result = price1.subtract(price3)
print(f"Subtraction: {result}")
