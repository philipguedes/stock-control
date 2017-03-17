# Imports here


class Clothes():
    def __init__(self, dateIn, trader, link, description="", cost=0, status="available", price=None, dateOut=None, paymentStatus="N/A"): # noqa
        self.cost = cost
        self.dateIn = dateIn
        self.trader = trader
        self.price = price
        self.dateOut = dateOut
        self.description = description
        self.status = status
        self.link = link
        self.paymentStatus = paymentStatus

    def reserve(self):
        self.status = "reserved"

    def updatePrice(self, price):
        self.price = price

    def sold(self, dateOut, paymentStatus="paid", price=None):
        self.status = "unavailable"
        self.dateOut = dateOut
        self.paymentStatus = paymentStatus
        if price:
            self.price = price
