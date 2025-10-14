# user_management.py

class UserManagement:
    def __init__(self):
        self.users = []

    def add_user(self, name):
        if name not in self.users:
            self.users.append(name)
            return "User added"
        else:
            return "User already exists"

    def remove_user(self, name):
        if name in self.users:
            self.users.remove(name)
            return "User removed"
        else:
            return "User not found"
