import logging
import time
from typing import Callable


def foo_square_calc(*args, **kwargs):
    a_side = float(input("Enter a_side parametr: "))
    b_side = float(input("Enter b_side parametr: "))
    result = a_side * b_side
    return f"Square = {result}."


def bar_range_counter(*args, **kwargs):
    number = int(input("Enter the number: "))
    for i in range(0, number + 1):
        print(i)
    return f"Top number in range is: {number}"


def var_fibo(*args, **kwargs):
    n = int(input("Enter a number: "))
    fibonacci_sequence = []
    a, b = 0, 1
    while a <= n:
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence


class TimerContextFunc:
    def __init__(self, func: Callable):
        self.func = func

    def __enter__(self):
        print("Processing...")
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        self.time_in_work = self.end_time - self.start_time
        logging.info(
            f"Function working time = {self.time_in_work}. Result: {self.func}"
        )


# Set up logging configuration
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

with TimerContextFunc(func=foo_square_calc()) as context:
    time.sleep(2)

with TimerContextFunc(func=bar_range_counter()) as context:
    time.sleep(3)

with TimerContextFunc(func=var_fibo()) as context:
    time.sleep(4)
