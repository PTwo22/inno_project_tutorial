# Software Testing Workshop

This workshop is designed to introduce you to various types of software testing using Python. We will explore unit testing, integration testing, system testing, and acceptance testing.
## Concept
- Software Testing 
- Deifferent types of Testing
    - Functional Testing
    - Non-Functional Testing
    - Structural Testing
    - Change-related Testing
- Level of Functional Testing
    - Unit Testing
    - Integration Testing 
    - System Testing
    - Acceptance Testing
- Different types of Non-Functional Testing
    - Performance Testing
    - Scalability Testing
    - Security Testing 
    - Usability Testing
    - Compatibility Testing
- Risk-Based Testing Approach
- Test Case Design Techniques
- Equivalence Partitioning
- BVA
- Decision Table Testing
- State Transition Testing 
- Pairwise Testing 
- Error Guessing
- Exploratory Testing
- Test Execution Process
- Defect Management Process
- Automated Testing

## Project Structure

```
.
├── acceptance_tests
│   ├── __init__.py
│   └── test_acceptance.py
├── requirements.txt
├── src
│   ├── __init__.py
│   ├── calculator.py
│   └── user_management.py
└── tests
    ├── __init__.py
    ├── integration
    │   ├── __init__.py
    │   └── test_user_calculator_integration.py
    ├── system
    │   ├── __init__.py
    │   └── test_system.py
    └── unit
        ├── __init__.py
        ├── test_calculator.py
        └── test_user_management.py
```

## Test Descriptions

### Unit Tests

Located in `tests/unit/`

1. `test_calculator.py`: Tests individual functions of the Calculator class.
2. `test_user_management.py`: Tests individual functions of the UserManagement class.

### Integration Tests

Located in `tests/integration/`

`test_user_calculator_integration.py`: Tests the interaction between UserManagement and Calculator classes.

### System Tests

Located in `tests/system/`

`test_system.py`: Tests the entire system workflow.

### Acceptance Tests

Located in `acceptance_tests/`

`test_acceptance.py`: Tests based on user stories to ensure the system meets user requirements.

## Running Tests

To run all tests:

```
python -m unittest discover
```

To run specific test types:

1. Unit tests: `python -m unittest discover tests/unit`
2. Integration tests: `python -m unittest discover tests/integration`
3. System tests: `python -m unittest discover tests/system`
4. Acceptance tests: `python -m unittest discover acceptance_tests`

## Generating Test Reports

To generate a detailed HTML report:

1. Install pytest and pytest-html if not already installed:
   ```
   pip install pytest pytest-html
   ```

2. Run the following command:
   ```
   pytest --html=report.html --self-contained-html
   ```

3. Open the generated `report.html` file in your web browser to view the detailed test results.

## Important Note

In the integration test file `test_user_calculator_integration.py`, there's a test case that is expected to fail:

```python
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
```

This test is designed to fail deliberately. It's testing a scenario where an unauthenticated user tries to use the calculator. In a real-world application, we would expect this to raise an exception or be prevented. However, our current implementation doesn't have this security check.

### Learning From Failing Tests

This failing test presents a valuable learning opportunity:

1. It demonstrates the importance of security in our application design.
2. It shows how tests can reveal gaps in our implementation.
3. It provides a chance to discuss how we might modify our Calculator or UserManagement classes to implement this security feature.

As you progress through the workshop, consider how you might modify the code to make this test pass. Would you add a check in the Calculator class for user authentication? Or would you modify the UserManagement class to control access to the Calculator? These are the kinds of design decisions that tests can help inform.

## Next Steps

1. Run all the tests and observe which ones pass and which fail.
2. Generate a test report and analyze the results.
3. Focus on the failing test in the integration tests. How would you modify the code to make it pass?
4. Consider adding more test cases to improve the test coverage of your code.

Remember, the goal of testing is not just to pass all tests, but to ensure our code behaves correctly and meets all requirements. Happy testing!
