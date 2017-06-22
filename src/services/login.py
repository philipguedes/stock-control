from flask_login import UserMixin
from src.services.firebase import Firebase


class UserClass(UserMixin):
    def __init__(self, firebase_data):
        self.data = firebase_data

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return True

    def get_id(self):
        return 0
