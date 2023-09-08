def foo():
    print("I am foo")
    return "Okey"


def bar(function):
    function.__call__()
    # print("I am bar")


def baz():
    yield 1
    yield 2
    yield 3
    yield 0
    yield 1
    yield 2
    yield 3
    yield 0


gen = baz()

bar.__call__(foo)
print(baz.__call__())
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
