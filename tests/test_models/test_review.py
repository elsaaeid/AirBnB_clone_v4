#!/usr/bin/python3
import unittest
import os
from models.review import Review


class TestReview(unittest.TestCase):
    """Unit tests for the Review class"""

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
        self.review_test = Review()
        self.review_test.user_id = "asd123"
        print("setUp")

    def tearDown(self):
        """Clean up the test"""
        print("tearDown")

    def test_review_documentation(self):
        """Check the documentation"""
        self.assertIsNotNone(Review.__doc__)
        self.assertIsNotNone(Review.__init__.__doc__)

    def test_review_existence(self):
        """Check if the review properties are created"""
        self.review_test.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertTrue(hasattr(self.review_test, "__init__"))
        self.assertTrue(hasattr(self.review_test, "text"))
        self.assertTrue(hasattr(self.review_test, "user_id"))
        self.assertTrue(hasattr(self.review_test, "place_id"))

    def test_model_to_dict(self):
        """Check converting to dict"""
        my_dict = self.review_test.to_dict()
        self.assertIsInstance(my_dict["id"], str)
        self.assertIsInstance(my_dict["user_id"], str)
        self.assertIsInstance(my_dict["created_at"], str)
        self.assertIsInstance(my_dict["updated_at"], str)

    def test_review_instance(self):
        """Check if review_test is an instance of Review"""
        self.assertIsInstance(self.review_test, Review)


if __name__ == '__main__':
    unittest.main()
