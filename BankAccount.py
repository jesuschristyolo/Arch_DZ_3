
class BankAccount:

    def __init__(self, card, balance, old_card):
        self.__card = card
        self.__balance = balance
        self.__old_card = old_card

        
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    @property
    def card(self):
        return self.__card





