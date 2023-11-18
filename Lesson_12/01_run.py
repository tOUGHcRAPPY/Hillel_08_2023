# from multiprocessing import Process
# from typing import TYPE_CHECKING
# from threading import Thread
# import sys
# from pprint import pprint as print

# sys.path.append("/Users/dmytroparfeniuk/Projects/hillel_08_2023")

# from services import Kitchen, Dish, DishSize

# if TYPE_CHECKING is True:
#     from services import Kitchen

# import importlib
# kitchen = importlib.import_module("kitchen")
# kitchen.Kitchen


# def main(kitchen: "Kitchen"):
#     pizza = Dish(
#         name="Peperoni",
#         size=DishSize.M,
#         ingredients=["tomato", "cheese", "peperoni", "dough"],
#     )

#     salad = Dish(
#         name="Caesar",
#         size=DishSize.S,
#         ingredients=["tomato", "cheese", "chicken", "dough"],
#     )

#     dishes = [pizza, salad]


# if __name__ == "__main__":
#     pass
# main()

# regular execution
# for dish in dishes:
#     Kitchen.cook(dish)

# concurrent execution
# threads = [
#     Thread(
#         target=Kitchen.cook,
#         args=(dish,),
#     )
#     for dish in dishes
# ]

# for thread in threads:
#     thread.start()

# for thread in threads:
#     thread.join()

# processes
# tasks = [Process(target=Kitchen.cook, args=[dish]) for dish in dishes]

# for task in tasks:
#     task.start()

# for task in tasks:
#     task.join()
