# Imports here


class Transaction():
    def __init__(self, link, transaction, data, address, person, trader):
        self.link = link
        self.transaction = transaction
        self.date = data
        self.address = address
        self.person = person
        self.trader = trader
        self.status = "pending"

    def finish(self):
        self.status = "finished"

    def cancel(self):
        self.status = "canceled"
