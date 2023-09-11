import functools

# MODIFY THIS DECORATOR
"""Replace the value of a dictionary with a 'masked' version."""


def mask_data(target_key: str, replace_with: str = "*"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            if "name" in data:
                data["name"] = "*" * len(data["name"])
            return data

        return wrapper

    return decorator


# TARGET FUNCTIONS
@mask_data(target_key="name")
def get_user(name: str, age: int):
    return {"name": name, "age": age}


# TEST OUPUT
print(get_user(name="Alice", age=30), get_user(name="Bob", age=25), sep="\n")
