def foo():
    return 1, 2, 3, 4, 5


data_1, data_2, data_3, data_4, data_5 = foo()
data_7 = foo()

# print(foo())
# print(data_1)
# print(data_1, data_2, data_3, data_4, data_5)
# print(type(data_1))
# print(data_7)

a, b, c = 10, 20, 30

# print(a, b, c)

user_contact_info = (
    "John",
    "Miller",
    "Arizona",
    "09675",
    "NoNumber",
    "male",
    45,
)
# name, surname, state, postal_code, tel_number, sex, age = user_contact_info
name, surname, state, *meta, age = user_contact_info

# print(name, surname, state)
# print(meta)
# print(type(meta))


# def create_user(name, surname, state, postal_code, tel_number, sex, age):
#     print("User has been created.")
#     print(f"Users name is {name}")
#     print(f"Users age is {age}")
#     print(f"Users sex is {sex}")


# create_user(
#     name="John",
#     surname="Miller",
#     state="Arizona",
#     postal_code="09675",
#     tel_number="NoNumber",
#     sex="male",
#     age=45,
# )

# create_user()


def create_user(*args, **kwargs):
    print("User has been created.")
    print(args)
    print(kwargs)


create_user(
    name="John",
    surname="Miller",
    state="Arizona",
    postal_code="09675",
    tel_number="NoNumber",
    sex="male",
    age=45,
)
