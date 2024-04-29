#!/usr/bin/python3
import unittest
import pep8
import inspect
from models.city import City
from models import storage
from models.base_model import BaseModel
import models


class TestCityDocs(unittest.TestCase):
    """Tests to check the documentation and style of City class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.city_functions = inspect.getmembers(City, inspect.isfunction)

    def test_pep8_equality(self):
        """Test that city.py and test_city.py conform to PEP8"""
        files_to_check = ['models/city.py',
                          'tests/test_models/test_city.py']
        style_guide = pep8.StyleGuide()
        total_errors = 0
        error_messages = []

        for file_path in files_to_check:
            with self.subTest(path=file_path):
                result = style_guide.check_files([file_path])
                errors = result.total_errors

                if errors > 0:
                    print(f"PEP8 errors in {file_path}:")
                    for error in result.messages:
                        error_messages.append(f"- {error}")
                total_errors += errors
        if total_errors > 0:
            error_message = f"Total PEP8 errors: {total_errors}\n"
            error_message += "\n".join(error_messages)
            self.fail(error_message)

    def test_city_module_docstring(self):
        """Test for the city.py module docstring"""
        self.assertIsNot(models.city.__doc__, None,
                         "city.py needs a docstring")
        self.assertTrue(len(models.city.__doc__) >= 1,
                        "city.py needs a docstring")

    def test_city_class_docstring(self):
        """Test for the City class docstring"""
        self.assertIsNot(City.__doc__, None,
                         "City class needs a docstring")
        self.assertTrue(len(City.__doc__) >= 1,
                "City class needs a docstring")

    def test_city_func_docstring(self):
        """Test for the presence of docstrings in City methods"""
        for func_name, func in self.city_functions:
            self.assertIsNot(
                func.__doc__,
                None,
                f"{func_name} method needs a docstring"
            )
            self.assertTrue(
                len(func.__doc__) >= 1,
                f"{func_name} method needs a docstring"
            )


class TestCity(unittest.TestCase):
    """Test the City class"""

    def test_is_subclass(self):
        """Test that City is a subclass of BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def setUp(self):
        """Set up the test environment"""
        self.city = City()

    def test_is_subclass_and_attributes(self):
        """Test that Place is a subclass of BaseModel and has attributes"""
        city = self.city
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        am = City()
        new_d = am.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertNotIn('_sa_instance_state', new_d)
        for attr in am.__dict__:
            if attr != "_sa_instance_state":
                self.assertIn(attr, new_d)
        self.assertIn('__class__', new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        am = City()
        new_d = am.to_dict()
        self.assertEqual(new_d["__class__"], "City")
        self.assertIsInstance(new_d["created_at"], str)
        self.assertIsInstance(new_d["updated_at"], str)
        self.assertEqual(am.created_at.strftime(t_format), new_d["created_at"])
        self.assertEqual(am.updated_at.strftime(t_format), new_d["updated_at"])

    def test_str(self):
        """test that the str method has the correct output"""
        city = City()
        string = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(string, str(city))

    def test_city_instance(self):
        """Test if City is an instance of the City class"""
        self.assertIsInstance(self.city, City)

    def test_city_save(self):
        """Test if the save function works for City"""
        old_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(old_updated_at, self.city.updated_at)

    def test_city_to_dict(self):
        """Test if the to_dict function works for City"""
        city_dict = self.city.to_dict()
        self.assertEqual(self.city.__class__.__name__, 'City')
        self.assertIsInstance(city_dict['created_at'], str)
        self.assertIsInstance(city_dict['updated_at'], str)

    def test_city_storage(self):
        """Test if City is correctly stored in the storage"""
        storage.new(self.city)
        storage.save()
        all_cities = storage.all(City)
        city_key = "City." + self.city.id
        self.assertIn(city_key, all_cities)

    def test_city_delete(self):
        """Test if the delete function works for City"""
        city_id = self.city.id
        storage.new(self.city)
        storage.save()
        storage.delete(self.city)
        all_cities = storage.all(City)
        city_key = "City." + city_id
        self.assertNotIn(city_key, all_cities)


if __name__ == '__main__':
    unittest.main()
