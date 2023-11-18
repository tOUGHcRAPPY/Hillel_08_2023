from dataclasses import dataclass
from enum import Enum
from multiprocessing import Process
from threading import Thread
from time import sleep


class DishSize(Enum):
    S = "S"
    M = "M"
    L = "L"


@dataclass
class Dish:
    name: str
    size: DishSize
    ingredients: list[str]


class Kitchen:
    @staticmethod
    def heat(dish: Dish):
        """This function is IO-bound task.
        We should wait till our dish is warming"""

        print(f"\n ⏲ Started heatting {dish.name}")
        # NOTE: IO-bound task
        sleep(3)
        print(f"\n 🍝 Your {dish} is heated!")

    @staticmethod
    def cook(dish: Dish):
        """This function is CPU-bound task.
        We should cook the meal.
        """
        print(f"\n ⏲ Started cooking {dish}")
        # NOTE: CPU-bound task
        _ = [i for i in range(120_000_000)]
        sleep(5)
        print(f"\n 🍝 Your {dish} is cooked!")


pasta = Dish(
    name="Carbonara",
    size=DishSize.M,
    ingredients=["cheese", "egg", "pasta", "becon"],
)

salad = Dish(
    name="Cesar",
    size=DishSize.L,
    ingredients=["salad", "tomato", "chicken", "sauce", "toast"],
)


def run():
    dishes = [pasta, salad]

    # NOTE: regular execution:

    print("Regular...")
    sleep(15)

    # NOTE: CPU-bound
    for dish in dishes:
        Kitchen.cook(dish)

    # NOTE: IO-bound
    for dish in dishes:
        Kitchen.heat(dish)

    # NOTE: concurrent execution:
    sleep(15)

    print("Threads...IO-bound")
    # NOTE: threads execution IO-bound
    threads = [
        Thread(
            target=Kitchen.heat,
            args=(dish,),
        )
        for dish in dishes
    ]

    print("Threads...CPU-bound")
    # NOTE: threads execution CPU-bound
    threads = [
        Thread(
            target=Kitchen.cook,
            args=(dish,),
        )
        for dish in dishes
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("☠️ All threads are finished.☠️")

    # NOTE: concurrent execution:
    sleep(15)

    print("Multiprocessing...CPU-bound")
    # NOTE: process execution CPU-bound
    cpu_tasks = [
        Process(
            target=Kitchen.cook,
            args=(dish,),
        )
        for dish in dishes
    ]

    print("Multiprocessing...IO-bound")
    #  NOTE: threads execution IO-bound
    io_tasks = [
        Process(
            target=Kitchen.heat,
            args=(dish,),
        )
        for dish in dishes
    ]

    for task in cpu_tasks:
        task.start()

    for task in cpu_tasks:
        task.join()

    for task in io_tasks:
        task.start()

    for task in io_tasks:
        task.join()

    print("☠️ All processes are finished.☠️")


if __name__ == "__main__":
    run()
