from ITicketRepo import ITicketRepo


class TicketProvider(ITicketRepo):

    def __init__(self, tickets=list):
        self.__tickets = tickets
        self.__status = False

    @property
    def get_tickets(self):
        return self.__tickets

    def update_ticket_status(self, value):
        if type(value) == bool:
            self.__status = value














