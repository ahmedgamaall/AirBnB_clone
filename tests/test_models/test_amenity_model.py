#!/usr/bin/python3
"""
Unittest for Amenity
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestAmenityClass(unittest.TestCase):
    """
    test class for Amenity class
    """
    amnty = Amenity()
    amnty.name = "Ahmed"
    amnty.id = "695-456-789"

    def test_defaults(self):
        """test default values for class attr"""

        a = Amenity()
        self.assertEqual(a.name, "")

    def test_object_without_kwargs(self):
        """
        create an object of Amenity class without kwargs
        """
        self.assertIsInstance(self.amnty, Amenity)
        self.assertIsInstance(self.amnty, BaseModel)
        self.assertIsInstance(self.amnty.id, str)
        self.assertIsInstance(self.amnty.created_at, datetime)
        self.assertIsInstance(self.amnty.updated_at, datetime)

        self.assertEqual(self.amnty.name, "Ahmed")
        self.assertEqual(self.amnty.id, "695-456-789")

    def test_object_with_kwargs(self):
        """
        create an object of Amenity class using kwargs
        """
        amnty_json = self.amnty.to_dict()
        n_amnty = Amenity(**amnty_json)
        self.assertIsInstance(n_amnty, Amenity)
        self.assertIsInstance(n_amnty.id, str)
        self.assertIsInstance(n_amnty.created_at, datetime)
        self.assertIsInstance(n_amnty.updated_at, datetime)
        self.assertEqual(n_amnty.name, "Ahmed")
        self.assertEqual(n_amnty.id, "695-456-789")
        self.assertNotEqual(n_amnty, self.amnty)
        self.assertDictEqual(n_amnty.__dict__, self.amnty.__dict__)

    def test_func_to_dict(self):
        """
            test to_dict class method
        """
        object_dict = self.amnty.to_dict()
        expect_dict = self.amnty.__dict__.copy()
        expect_dict["__class__"] = self.amnty.__class__.__name__
        expect_dict["updated_at"] = self.amnty.updated_at.isoformat()
        expect_dict["created_at"] = self.amnty.created_at.isoformat()
        self.assertDictEqual(expect_dict, object_dict)

    def test_func_save(self):
        """"
            test save class method
        """
        bf_update = self.amnty.updated_at
        self.amnty.name = "Ahmed"
        self.amnty.save()
        af_update = self.amnty.updated_at
        self.assertNotEqual(bf_update, af_update)

    def test_func_str(self):
        """
            test str class method
        """
        s = self.amnty.__class__.__name__

        exp_string = f"[{s}] ({self.amnty.id}) {self.amnty.__dict__}"
        self.assertEqual(self.amnty.__str__(), exp_string)

if __name__ == '__main__':
    unittest.main()
