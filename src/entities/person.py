# Imports here


class Person():

    def __init__(self, name, address, phone, facebook=None, instagram=None):
        self.name = name
        self.address = address
        self.phone = phone
        self.facebook = facebook
        self.instagram = instagram
        self.comments = []

    def updateFacebook(self, facebook):
        self.facebook = facebook

    def updateInstagram(self, instagram):
        self.instagram = instagram

    def addComment(self, comment):
        self.comments.append(comment)

    def updateProbeAddress(self, address):
        self.address['probe'] = address

    def updateDeliveryAddress(self, address):
        self.address['delivery'] = address
