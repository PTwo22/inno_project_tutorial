import unittest
from src.calculator import Calculator
from src.user_management import UserManagement

class TestSystem(unittest.TestCase):
    def setUp(self):
        self.um = UserManagement()
        self.calc = Calculator()

    def test_full_system_flow(self):
        # 1. Add user
        self.um.add_user("system_user", "syspass")

        # 2. Authenticate user
        self.assertTrue(self.um.authenticate("system_user", "syspass"))

        # 3. Perform a series of calculations
        result_add = self.calc.add(10, 5)
        result_subtract = self.calc.subtract(result_add, 3)
        result_multiply = self.calc.multiply(result_subtract, 2)
        result_divide = self.calc.divide(result_multiply, 4)

        # 4. Verify the final result
        self.assertEqual(result_divide, 6)

        # 5. Remove user
        self.um.remove_user("system_user")

        # 6. Confirm the user has been removed
        with self.assertRaises(ValueError):
            self.um.remove_user("system_user")

if __name__ == '__main__':
    unittest.main()
