#!/usr/bin/python3
import unittest
import os
from models.user import User


class TestUser(unittest.TestCase):
    """Unit tests for the User class"""

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
        self.user_test = User()
        self.user_test.first_name = 'Said'
        self.user_test.last_name = "Ellithy"
        self.user_test.email = 'saidsadaoy@gmail.com'
        self.user_test.password = "root"
        print("setUp")

    def tearDown(self):
        """Clean up the test"""
        print("tearDown")

    def test_user_documentation(self):
        """Check the documentation"""
        self.assertIsNotNone(User.__doc__)
        self.assertIsNotNone(User.__init__.__doc__)

    def test_user_properties(self):
        """Check if the user properties are created"""
        self.user_test.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertTrue(hasattr(self.user_test, "__init__"))
        self.assertTrue(hasattr(self.user_test, "first_name"))
        self.assertTrue(hasattr(self.user_test, "last_name"))
        self.assertTrue(hasattr(self.user_test, "email"))
        self.assertTrue(hasattr(self.user_test, "password"))

    def test_user_first_name(self):
        """Check if the first name is created"""
        self.assertEqual(self.user_test.first_name, 'Said')

    def test_user_last_name(self):
        """Check if the last name is created"""
        self.assertEqual(self.user_test.last_name, "Ellithy")

    def test_user_email(self):
        """Check if the email is created"""
        self.assertEqual(self.user_test.email, 'saidsadaoy@gmail.com')

    def test_user_password(self):
        """Check if the password is created"""
        self.assertEqual(self.user_test.password, "root")

    def test_model_to_dict(self):
        """Check converting to dict"""
        my_dict = self.user_test.to_dict()
        self.assertIsInstance(my_dict["id"], str)
        self.assertIsInstance(my_dict["email"], str)
        self.assertIsInstance(my_dict["created_at"], str)
        self.assertIsInstance(my_dict["updated_at"], str)

    def test_user_instance(self):
        """Check if user_test is an instance of User"""
        self.assertIsInstance(self.user_test, User)


if __name__ == '__main__':
    unittest.main()
