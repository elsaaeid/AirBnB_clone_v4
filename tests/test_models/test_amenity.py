#!/usr/bin/python3
import unittest
from models.amenity import Amenity
from datetime import datetime
import os
import json

Amenity = Amenity
storage_type = os.environ.get('HBNB_TYPE_STORAGE')


class TestAmenity(unittest.TestCase):
    """Class for testing Amenity documentation"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('........   Amenity  Class   ........')
        print('.................................\n\n')

    def test_doc_file(self):
        """Test documentation for the file"""
        expected = '\nAmenity Class from Models Module\n'
        actual = Amenity.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """Test documentation for the class"""
        expected = 'Amenity class handles all application amenities'
        actual = Amenity.__doc__
        self.assertEqual(expected, actual)


class TestAmenityInstances(unittest.TestCase):
    """Testing for class instances"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('....... Testing Functions .......')
        print('.........  Amenity  Class  .........')
        print('.................................\n\n')

    def setUp(self):
        """Initialize a new Amenity for testing"""
        self.amenity = Amenity()

    def test_instantiation(self):
        """Check if Amenity is properly instantiated"""
        self.assertIsInstance(self.amenity, Amenity)

    @unittest.skipIf(storage_type == 'db', 'skip if environ is db')
    def test_to_string(self):
        """Check if Amenity is properly casted to string"""
        my_str = str(self.amenity)
        my_list = ['Amenity', 'id', 'created_at']
        actual = sum(sub_str in my_str for sub_str in my_list)
        self.assertEqual(actual, 3)

    @unittest.skipIf(storage_type == 'db', 'skip if environ is db')
    def test_instantiation_no_updated(self):
        """Should not have updated attribute"""
        my_str = str(self.amenity)
        self.assertNotIn('updated_at', my_str)

    @unittest.skipIf(storage_type == 'db', 'skip if environ is db')
    def test_updated_at(self):
        """Save function should add updated_at attribute"""
        self.amenity.save()
        self.assertIsInstance(self.amenity.updated_at, datetime)

    @unittest.skipIf(storage_type == 'db', 'skip if environ is db')
    def test_to_json(self):
        """to_json should return serializable dict object"""
        amenity_json = self.amenity.to_json()
        self.assertIsInstance(amenity_json, dict)
        self.assertTrue(all(isinstance(value, (str, int)) for value in amenity_json.values()))

    @unittest.skipIf(storage_type == 'db', 'skip if environ is db')
    def test_json_class(self):
        """to_json should include class key with value Amenity"""
        amenity_json = self.amenity.to_json()
        self.assertEqual(amenity_json['__class__'], 'Amenity')

    def test_amenity_attribute(self):
        """Add amenity attribute"""
        self.amenity.name = "greatWifi"
        self.assertEqual(self.amenity.name, "greatWifi")


if __name__ == '__main__':
    unittest.main()
