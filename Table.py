from Party import *

class Table:
    def __init__(self, table_number, table_size):
        self.table_number = table_number
        self.table_size = table_size
        self.table_availability = True
        self.party = Party(0,0,True)

    def table_join(self, party):
        self.party = party
        self.table_availability = False

    def table_left(self):
        self.party.party_size = 0
        self.party.party_number = 0
        self.party.waiting = True
        self.table_availability = True