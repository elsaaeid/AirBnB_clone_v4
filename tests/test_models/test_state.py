#!/usr/bin/python3
import unittest
import os
from models.state import State


class TestState(unittest.TestCase):
    """Unit tests for the State class"""

    @classmethod
    def setUpClass(cls):
        """Set up the class"""
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        """Clean up the class"""
        print("tearDownClass")

    def setUp(self):
        """Set up the test"""
        self.state_test = State()
        print("setUp")

    def tearDown(self):
        """Clean up the test"""
        print("tearDown")

    def test_state_documentation(self):
        """Check the documentation"""
        self.assertIsNotNone(State.__doc__)
        self.assertIsNotNone(State.__init__.__doc__)

    def test_state_existence(self):
        """Check if the state properties are created"""
        self.state_test.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertTrue(hasattr(self.state_test, "__init__"))
        self.assertTrue(hasattr(self.state_test, "name"))

    def test_state_name(self):
        """Check if the state name is created"""
        self.state_test.name = 'Great'
        self.assertEqual(self.state_test.name, 'Great')

    def test_model_to_dict(self):
        """Check converting to dict"""
        my_dict = self.state_test.to_dict()
        self.assertIsInstance(my_dict["created_at"], str)
        self.assertIsInstance(my_dict["updated_at"], str)

    def test_state_instance(self):
        """Check if state_test is an instance of State"""
        self.assertIsInstance(self.state_test, State)


if __name__ == '__main__':
    unittest.main()
