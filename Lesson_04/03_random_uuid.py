from typing import Generator
from uuid import UUID, uuid4

# UUID Generator with UUID v4:

# used_uuid_set: set[UUID] = set()

# def generate_uuid() -> UUID:
#     while True:
#       generated_uuid = uuid4()
#       if generated_uuid not in used_uuid_set:
#           used_uuid_set.add(generated_uuid)
#           return generated_uuid
      

def uuid_from_generator() -> Generator[UUID, None, None]:
   used_uuid_set: set[UUID] = set()
   while True:
      generated_uuid = uuid4()
      if generated_uuid not in used_uuid_set:
         used_uuid_set.add(generated_uuid)
         yield generated_uuid

uuid = uuid_from_generator()
      
      
print(next(uuid))
print(next(uuid))
print(next(uuid))


used_uuid_dict_by_user: dict[str, set[UUID]] = {}

# {
#    "John": {304f94c0-1dca-403b-8969-fc52cc590852, ...}
#    "Marry": {5abc5dba-e45c-4782-8074-7abb55db01d3, ...}
# }

def generate_uuid_from_function(user: str) -> UUID:
    while True:
      generated_uuid = uuid4()
      if generated_uuid not in used_uuid_dict_by_user[user]:
          used_uuid_dict_by_user[user].add(generated_uuid)
          return generated_uuid
      
john_uuid = uuid_from_generator()
marry_uuid = uuid_from_generator()

print(type(john_uuid))

print("John: " + str(next(john_uuid)))
print("John: " + str(next(john_uuid)))
print("Marry: " + str(next(marry_uuid)))