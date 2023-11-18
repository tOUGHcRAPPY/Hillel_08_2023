from functools import singledispatch


@singledispatch
def add(a, b):
    raise NotImplementedError("Unsupported type.")


@add.register(int)
def _(a, b):
    return a + b


@add.register(str)
def _(a, b):
    return f"Concat {a}{b}"


print(add(1, 1))
print(add("1", "1"))
