import unittest
from src.calculator import Calculator
from src.user_management import UserManagement

class TestAcceptance(unittest.TestCase):
    def setUp(self):
        self.um = UserManagement()
        self.calc = Calculator()

    def test_user_story_1(self):
        """
        User Story 1: As a new user, I want to register an account, log in to the system, and perform basic calculations.
        """
        # Step 1: Register a new user
        self.um.add_user("new_user", "password123")

        # Step 2: Verify that the user can log in
        self.assertTrue(self.um.authenticate("new_user", "password123"))

        # Step 3: Perform basic calculations
        result_add = self.calc.add(15, 7)
        self.assertEqual(result_add, 22)

        result_subtract = self.calc.subtract(50, 30)
        self.assertEqual(result_subtract, 20)

        result_multiply = self.calc.multiply(6, 4)
        self.assertEqual(result_multiply, 24)

        result_divide = self.calc.divide(100, 5)
        self.assertEqual(result_divide, 20)

    def test_user_story_2(self):
        """
        User Story 2: As an existing user, I want to perform a series of complex calculations and ensure the accuracy of the results.
        """
        # Step 1: Log in using an existing user
        self.um.add_user("power_user", "strongpass")
        self.assertTrue(self.um.authenticate("power_user", "strongpass"))

        # Step 2: Perform complex calculations
        result = self.calc.add(100, 50)  # 150
        result = self.calc.multiply(result, 2)  # 300
        result = self.calc.subtract(result, 75)  # 225
        result = self.calc.divide(result, 5)  # 45

        # Step 3: Verify the final result
        self.assertEqual(result, 45)

if __name__ == '__main__':
    unittest.main()

