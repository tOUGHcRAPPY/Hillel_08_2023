from dataclasses import dataclass
from typing import Dict

EXCHANGE_RATES: Dict[str, Dict[str, float]] = {
    "USD": {
        "USD": 1.0,
        "UAH": 36.6,
        "EUR": 0.96,
        "GBP": 0.83,
        "MXN": 17.9,
        "CAD": 1.37,
        "PLN": 4.42,
        "CHF": 0.92,
        "RUB": 99.2,
        "CNY": 7.32,
    },
    "UAH": {
        "USD": 0.03,
        "UAH": 1.0,
        "EUR": 0.02,
        "GBP": 0.02,
        "MXN": 0.5,
        "CAD": 0.04,
        "PLN": 0.12,
        "CHF": 0.02,
        "RUB": 2.7,
        "CNY": 0.2,
    },
    "EUR": {
        "USD": 1.05,
        "UAH": 38.4,
        "EUR": 1.0,
        "GBP": 0.87,
        "MXN": 18.74,
        "CAD": 1.43,
        "PLN": 4.62,
        "CHF": 0.96,
        "RUB": 104.3,
        "CNY": 7.7,
    },
    "GBP": {
        "USD": 1.2,
        "UAH": 44.6,
        "EUR": 1.15,
        "GBP": 1.0,
        "MXN": 21.4,
        "CAD": 1.65,
        "PLN": 5.33,
        "CHF": 1.1,
        "RUB": 120.06,
        "CNY": 8.9,
    },
    "MXN": {
        "USD": 0.06,
        "UAH": 2.09,
        "EUR": 0.05,
        "GBP": 0.04,
        "MXN": 1.0,
        "CAD": 0.07,
        "PLN": 0.25,
        "CHF": 0.05,
        "RUB": 5.6,
        "CNY": 0.4,
    },
    "CAD": {
        "USD": 0.73,
        "UAH": 27.0,
        "EUR": 0.7,
        "GBP": 0.6,
        "MXN": 12.93,
        "CAD": 1.0,
        "PLN": 3.2,
        "CHF": 0.7,
        "RUB": 72.5,
        "CNY": 5.35,
    },
    "PLN": {
        "USD": 0.23,
        "UAH": 8.4,
        "EUR": 0.22,
        "GBP": 0.19,
        "MXN": 4.0,
        "CAD": 0.3,
        "PLN": 1.0,
        "CHF": 0.21,
        "RUB": 22.5,
        "CNY": 1.66,
    },
    "CHF": {
        "USD": 1.1,
        "UAH": 40.2,
        "EUR": 1.04,
        "GBP": 0.9,
        "MXN": 19.3,
        "CAD": 1.5,
        "PLN": 4.8,
        "CHF": 1.0,
        "RUB": 108.04,
        "CNY": 8.0,
    },
    "RUB": {
        "USD": 0.01,
        "UAH": 0.37,
        "EUR": 0.009,
        "GBP": 0.008,
        "MXN": 0.18,
        "CAD": 0.014,
        "PLN": 0.044,
        "CHF": 0.009,
        "RUB": 1.0,
        "CNY": 0.074,
    },
    "CNY": {
        "USD": 0.14,
        "UAH": 5.05,
        "EUR": 0.13,
        "GBP": 0.11,
        "MXN": 2.42,
        "CAD": 0.19,
        "PLN": 0.6,
        "CHF": 0.13,
        "RUB": 13.56,
        "CNY": 1.0,
    },
}


@dataclass
class Price:
    amount: float
    currency: str

    def convert(self, target: str) -> "Price":
        currency_rate = EXCHANGE_RATES[self.currency][target]
        return Price(amount=self.amount * currency_rate, currency=target)

    def __add__(self, other: "Price") -> "Price":
        """
        1. When script is working with two instances of class Price
        and both of them has currency NOT USD:
          self(!USD) + other(!USD)
          self(!USD) => self(USD)
          other(!USD) => other(USD)
          result = self(USD) + other(USD)
          result(USD) => result(!USD)
          return result(!USD)

        2. When script is working with two instances of class Price
        and one of them (OTHER) has currency NOT USD:
          self(USD) + other(!USD)
          other(!USD) => other(USD)
          result = self(USD) + other(USD)
          return result

        3. When script is working with two instances of class Price
        and both of them has currency USD:
          result = self(USD) + other(USD)
          return result
        """

        if self.currency.upper() != "USD" and other.currency.upper() != "USD":
            self_converted: "Price" = self.convert("USD")
            other_converted: "Price" = other.convert("USD")
            result_converted = Price(
                amount=(self_converted.amount + other_converted.amount),
                currency="USD",
            )
            # print(self_converted.amount, other_converted.amount)
            # print(result_converted)
            return result_converted.convert(target=self.currency)

    def __sub__(self, other: "Price") -> "Price":
        """
        1. When script is working with two instances of class Price
        and both of them has currency NOT USD:
          self(!USD) - other(!USD)
          self(!USD) => self(USD)
          other(!USD) => other(USD)
          result = self(USD) - other(USD)
          result(USD) => result(!USD)
          return result(!USD)

        2. When script is working with two instances of class Price
        and one of them (OTHER) has currency NOT USD:
          self(USD) - other(!USD)
          other(!USD) => other(USD)
          result = self(USD) - other(USD)
          return result

        3. When script is working with two instances of class Price
        and both of them has currency USD:
          result = self(USD) - other(USD)
          return result
        """
        if self.currency.upper() != "USD" and other.currency.upper() != "USD":
            self_converted: "Price" = self.convert("USD")
            other_converted: "Price" = other.convert("USD")
            result_converted = Price(
                amount=(self_converted.amount - other_converted.amount),
                currency="USD",
            )
            # print(self_converted.amount, other_converted.amount)
            # print(result_converted)
            return result_converted.convert(target=self.currency)


left = Price(amount=100, currency="UAH")
right = Price(amount=100, currency="CAD")

left_1 = Price(amount=1000, currency="UAH")
right_1 = Price(amount=10, currency="CAD")

result_1: Price = left + right
result_2: Price = left_1 - right_1

print(result_1)
print(result_2)
