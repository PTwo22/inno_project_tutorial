import unittest
from src.user_management import UserManagement

class TestUserManagement(unittest.TestCase):
    def setUp(self):
        self.um = UserManagement()

    def test_add_user(self):
        self.um.add_user("alice", "password123")
        self.assertTrue("alice" in self.um.users)
        self.assertEqual(self.um.users["alice"], "password123")

    def test_add_existing_user(self):
        self.um.add_user("bob", "password456")
        with self.assertRaises(ValueError):
            self.um.add_user("bob", "newpassword")

    def test_authenticate(self):
        self.um.add_user("charlie", "securepass")
        self.assertTrue(self.um.authenticate("charlie", "securepass"))
        self.assertFalse(self.um.authenticate("charlie", "wrongpass"))
        self.assertFalse(self.um.authenticate("david", "anypass"))

    def test_remove_user(self):
        self.um.add_user("eve", "evepass")
        self.um.remove_user("eve")
        self.assertFalse("eve" in self.um.users)

    def test_remove_nonexistent_user(self):
        with self.assertRaises(ValueError):
            self.um.remove_user("nonexistent")

if __name__ == '__main__':
    unittest.main()
