# Imports here


class Clothes():
    def __init__(self, dateIn, trader, link, price, cost, description="", status="available"): # noqa
        self.cost = cost
        self.dateIn = dateIn
        self.trader = trader
        self.price = price
        self.description = description
        self.status = status
        self.link = link

    def reserve(self):
        self.status = "reserved"

    def updatePrice(self, price):
        self.price = price

    def sold(self, dateOut, price, paymentStatus="paid"):
        self.status = "unavailable"
        self.dateOut = dateOut
        self.paymentStatus = paymentStatus
        self.price = price
