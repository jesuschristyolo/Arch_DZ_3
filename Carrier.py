class Carrier:

    def __init__(self, id: int, zones: int, card_number: int):
        self.__id = id
        self.__zones = zones
        self.__card_number = card_number

    @property
    def id(self):
        return self.__id

    @property
    def card_number(self):
        return self.__card_number
