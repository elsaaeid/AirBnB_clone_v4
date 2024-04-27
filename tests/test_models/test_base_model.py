#!/usr/bin/python3
import unittest
import os
from models import storage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unit tests for testing the instantiation of the BaseModel class"""

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
        self.my_model = BaseModel()
        self.my_model.my_number = 29
        print("setUp")

    def tearDown(self):
        """Clean up the test"""
        print("tearDown")

    def test_models_documentation(self):
        """Check the documentation"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_models_name(self):
        """Check if name is created"""
        self.my_model.name = 'test'
        self.assertEqual(self.my_model.name, 'test')

    def test_models_number(self):
        """Check if the number is created"""
        self.assertEqual(self.my_model.my_number, 29)

    def test_models_existence(self):
        """Check if the json file and methods exist"""
        self.my_model.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertTrue(hasattr(self.my_model, "__init__"))
        self.assertTrue(hasattr(self.my_model, "__str__"))
        self.assertTrue(hasattr(self.my_model, "save"))
        self.assertTrue(hasattr(self.my_model, "to_dict"))

    def test_models_non_empty(self):
        """Check if the json file is not empty"""
        with open('file.json', 'r') as file:
            data = file.read()
            self.assertTrue(data)

    def test_models_save(self):
        """Check if the save function works"""
        a = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(a, self.my_model.updated_at)
        self.assertNotEqual(self.my_model.created_at, self.my_model.updated_at)

    def test_models_instance(self):
        """Check if my_model is an instance of BaseModel"""
        self.assertIsInstance(self.my_model, BaseModel)

    def test_models_to_dict(self):
        """Test the to_dict method of the BaseModel class"""
        my_dict = self.my_model.to_dict()
        self.assertIsInstance(my_dict["created_at"], str)
        self.assertIsInstance(my_dict["updated_at"], str)
        self.assertIsInstance(my_dict["my_number"], int)
        self.assertIsInstance(my_dict["id"], str)


if __name__ == '__main__':
    unittest.main()
