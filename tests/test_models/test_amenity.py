#!/usr/bin/python3
import unittest
import os
from models import Amenity


class TestAmenity(unittest.TestCase):
    """Unit tests for the Amenity class"""

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
        self.amenity_test = Amenity()
        print("setUp")

    def tearDown(self):
        """Clean up the test"""
        print("tearDown")

    def test_amenity_documentation(self):
        """Check the documentation"""
        self.assertIsNotNone(Amenity.__doc__)
        self.assertIsNotNone(Amenity.__init__.__doc__)

    def test_amenity_existence(self):
        """Check if the Amenity methods exist"""
        self.amenity_test.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertTrue(hasattr(self.amenity_test, "__init__"))
        self.assertTrue(hasattr(self.amenity_test, "name"))

    def test_amenity_name(self):
        """Check if the name is created"""
        self.amenity_test.name = 'Good'
        self.assertEqual(self.amenity_test.name, 'Good')

    def test_amenity_instance(self):
        """Check if amenity_test is an instance of Amenity"""
        self.assertIsInstance(self.amenity_test, Amenity)

    def test_amenity_to_dict(self):
        """Test the to_dict method of the Amenity class"""
        my_dict = self.amenity_test.to_dict()
        self.assertIsInstance(my_dict["created_at"], str)
        self.assertIsInstance(my_dict["updated_at"], str)
        self.assertIsInstance(my_dict["id"], str)


if __name__ == '__main__':
    unittest.main()
