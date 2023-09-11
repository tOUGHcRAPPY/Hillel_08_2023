def name_hider(name: str):
    hided_name = name.replace(name, "*" * len(name))
    print(hided_name)
    return hided_name


def name_hider_in_dictionary(name: str, age: int):
    data = {"name": name, "age": age}
    if "name" in data:
        data["name"] = name.replace(name, "*" * len(name))
        print(data)
    return data


def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("hello...")
        func(*args, **kwargs)
        print("fuck you!")

    return wrapper


@decorator_func
def get_user(name: str, age: int):
    print({"name": name, "age": age})
    return {"name": name, "age": age}


get_user("Alex", 13)


def square_calc(a_side: int, b_side: int):
    square = a_side * b_side
    print(f"The square of your figure is {square}.")
    return square


square_calc(5, 7)


def calc_decorator(func):
    def wrapper(*args, **kwargs):
        calculation = func(*args, **kwargs)
        a_side, b_side = args
        if a_side == b_side:
            print("Your figure is square-shaped.")
        else:
            print("Your figure is rectangular-shaped.")
        return calculation

    return wrapper


@calc_decorator
def square_calc(a_side: int, b_side: int):
    square = a_side * b_side
    print(f"The square of your figure is {square}.")
    return square


square_calc(9, 9)

list_of_numbers = [{"odd": [], "even": []}]


def categorize_numbers(func):
    def wrapper(*args):
        for number in args:
            if number % 2 == 0:
                list_of_numbers[0]["even"].append(number)
            else:
                list_of_numbers[0]["odd"].append(number)

    return wrapper


@categorize_numbers
def add_number_to_list(*args):
    list_of_numbers.append(*args)


add_number_to_list(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


print(list_of_numbers)
