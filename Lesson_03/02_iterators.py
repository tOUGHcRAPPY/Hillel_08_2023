names: list[str] = ["John", "Marry"]

_names = iter(names)
print(_names.__next__())
print(_names.__next__())
print(_names.__next__())


class Iterator:
    def __iter__(self):
        pass

    def __next__(self):
        pass


instances = Iterator()
for instance in instances:
    print(instance)

while True:
    # name = _name.__next__()
    try:
        value = next(_names)
        print(f"{value=}")
    except StopIteration:
        break

# for name in _names:
# print(f"{name=}")
