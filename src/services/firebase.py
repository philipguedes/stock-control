import pyrebase


class Firebase():

    def __init__(self):
        self.config = {
            "apiKey": "AIzaSyD0eLizDX0GWzSWF507dg9_PVUxYHA7ycs",
            "authDomain": "brecho-das-4.firebaseapp.com",
            "databaseURL": "https://brecho-das-4.firebaseio.com",
            "storageBucket": "",
            "messagingSenderId": "369494205719"
        }
        self.firebase = pyrebase.initialize_app(self.config)
        self.db = self.firebase.database()
        self.users = []

    def authenticate(self, email, password):
        auth = self.firebase.auth()
        user = auth.sign_in_with_email_and_password(email, password)
        return user

    def insert_new_cloth(self, cloth, user):
        data = cloth.__dict__
        # TODO
        # Parse instagram_id
        instagram_id = "fix me"
        self.db.child("Cloth").child(instagram_id).push(data, user['idToken'])

    def insert_new_person(self, cloth):
        pass
