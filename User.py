class Descriptor:

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class User:
    id = Descriptor()
    user_name = Descriptor()
    hash_password = Descriptor()
    phone = Descriptor()
    benefits = Descriptor()
    card_number = Descriptor()

    def __init__(self, id: int, user_name: str, hash_password: int, phone: int, benefits: str, card_number: int):
        self.id = id
        self.user_name = user_name
        self.hash_password = hash_password
        self.phone = phone
        self. benefits = benefits
        self.card_number = card_number




















