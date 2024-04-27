#!/usr/bin/python3
import unittest
import os
from models.city import City


class TestCity(unittest.TestCase):
    """Unit tests for the City class"""

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
        self.city_test = City()
        self.city_test.state_id = "100"
        print("setUp")

    def tearDown(self):
        """Clean up the test"""
        print("tearDown")

    def test_city_documentation(self):
        """Check the documentation"""
        self.assertIsNotNone(City.__doc__)
        self.assertIsNotNone(City.__init__.__doc__)

    def test_city_existence(self):
        """Check if the city methods exist"""
        self.city_test.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertTrue(hasattr(self.city_test, "__init__"))
        self.assertTrue(hasattr(self.city_test, "state_id"))
        self.assertTrue(hasattr(self.city_test, "name"))

    def test_city_name(self):
        """Check if the name is created"""
        self.city_test.name = 'Paris'
        self.assertEqual(self.city_test.name, 'Paris')

    def test_city_instance(self):
        """Check if city_test is an instance of City"""
        self.assertIsInstance(self.city_test, City)

    def test_city_to_dict(self):
        """Test the to_dict method of the City class"""
        my_dict = self.city_test.to_dict()
        self.assertIsInstance(my_dict["created_at"], str)
        self.assertIsInstance(my_dict["updated_at"], str)
        self.assertIsInstance(my_dict["state_id"], str)
        self.assertIsInstance(my_dict["id"], str)


if __name__ == '__main__':
    unittest.main()
