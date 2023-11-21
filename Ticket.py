import datetime


class Descriptor:

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Ticket:
    id = Descriptor()
    price = Descriptor()
    data = Descriptor()
    zone_start = Descriptor()
    zone_stop = Descriptor()
    type = Descriptor()
    route_number = Descriptor()
    place = Descriptor()
    is_valid = Descriptor()

    def __init__(self, id: int, price: int, data: datetime.date, zone_start: int, zone_stop: int,
                 type: int, route_number: int, place: int, is_valid: bool):
        self.__id = id
        self.__price = price
        self.__data = data
        self.__zone_start = zone_start
        self.__zone_stop = zone_stop
        self.__type = type
        self.__route_number = route_number
        self.__place = place
        self.__is_valid = is_valid


t = Ticket(1, 2, datetime.date(2010, 4, 5), 4, 5, 6, 7, 8, True)
t.place = 20
print(t.place)
print(t.__dict__)


