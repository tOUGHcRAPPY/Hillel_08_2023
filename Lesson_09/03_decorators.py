# def staticmethod(func):
#     def inner(*args, **kwargs):
#         if "self" in args:
#             self.del from args
#         return func(*args, **kwargs)
#     return inner


class Shop:
    SHOP_USERS_MAX_SIZE = 300

    def register(self, username, password1, password2, email):
        pass

    def login(self, username, password):
        pass

    @staticmethod
    def get_all_users_amount(user_card_info):
        # number = SELECT COUNT(id) FROM users:
        return 12

    @classmethod
    def build_new(cls, domain: str):
        # Host the application on {domain}
        cls.SHOP_USERS_MAX_SIZE
        cls.login()
        # cls == Shop
        # cls.login() == Shop.login()

    def buy(self, product: dict):
        pass


zara = Shop()
zippo = Shop()

zara.build_new("zara.com")
Shop.build_new("zippo.com")

zara.buy({"Hat": 1000})

# same as:

Shop.buy(zara, {"Hat": 1000})
