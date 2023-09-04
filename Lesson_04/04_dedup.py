import sys
from pympler.asizeof import asizeof

users: list[str] = ["John", "Marry", "Jack", "Helen", "John", "Marry"]

# users_seen = set()
# for user in users:
#     if user in users_seen:
#         continue
#     else:
#         users_seen.add(user)
#         print(user)
        

def dedup(collection):
    items = set()
    for item in collection:
        if item in items:
            continue
        yield item
        items.add(item)


for user in dedup(users):
    print(user)


print(sys.getsizeof(users))
print(asizeof(users))