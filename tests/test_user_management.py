# tests/test_user_management.py

from user_management import UserManagement  # adjust class name if different

def test_add_user():
    um = UserManagement()
    result = um.add_user("John")  # adjust method according to your code
    assert result == "User added"
