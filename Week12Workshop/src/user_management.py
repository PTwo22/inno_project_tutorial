class UserManagement:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            raise ValueError("Username already exists")
        self.users[username] = password

    def authenticate(self, username, password):
        if username not in self.users:
            return False
        return self.users[username] == password

    def remove_user(self, username):
        if username not in self.users:
            raise ValueError("User does not exist")
        del self.users[username]
