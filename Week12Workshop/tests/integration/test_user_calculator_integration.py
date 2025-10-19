import unittest
from src.calculator import Calculator
from src.user_management import UserManagement

class TestUserCalculatorIntegration(unittest.TestCase):
    def setUp(self):
        self.um = UserManagement()
        self.calc = Calculator()

    def test_authenticated_calculation(self):
        # Add User
        self.um.add_user("math_user", "mathpass")

        # Authenticate and perform calculation
        if self.um.authenticate("math_user", "mathpass"):
            result = self.calc.add(5, 3)
            self.assertEqual(result, 8)
        else:
            self.fail("Authentication failed")

    def test_unauthenticated_calculation(self):
        # Attempt to perform calculation with unauthenticated user
        if not self.um.authenticate("unknown_user", "wrongpass"):
            with self.assertRaises(Exception):
                # In the actual application, we assume that unauthenticated users cannot access the calculator.
                # In this test, we expect an exception to be raised.
                # However, at this stage, the test will fail.
                self.calc.add(5, 3)
        else:
            self.fail("Authentication should have failed")

if __name__ == '__main__':
    unittest.main()
