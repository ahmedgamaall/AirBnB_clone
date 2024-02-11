#!/usr/bin/python3
"""
Unittest for Review class model
"""
import unittest
from models.review import Review
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestReviewClass(unittest.TestCase):
    """
    test class for Review class
    """
    rvw = Review()
    rvw.place_id = "p-987456"
    rvw.user_id = "u-654123"
    rvw.text = "It's nice"

    def test_defaults(self):
        """test default values"""

        r = Review()
        self.assertEqual(r.place_id, "")
        self.assertEqual(r.user_id, "")
        self.assertEqual(r.text, "")

    def test_object_without_kwargs(self):
        """
        create an object of Review class without kwargs
        """
        self.assertIsInstance(self.rvw, Review)
        self.assertIsInstance(self.rvw, BaseModel)
        self.assertIsInstance(self.rvw.id, str)
        self.assertIsInstance(self.rvw.created_at, datetime)
        self.assertIsInstance(self.rvw.updated_at, datetime)
        self.assertIsInstance(self.rvw.place_id, str)
        self.assertIsInstance(self.rvw.user_id, str)
        self.assertIsInstance(self.rvw.text, str)
        self.assertEqual(self.rvw.place_id, "p-987456")
        self.assertEqual(self.rvw.user_id, "u-654123")
        self.assertEqual(self.rvw.text, "It's nice")

    def test_object_with_kwargs(self):
        """
        create an object of Review class using kwargs
        """
        data = {
            "id": "r-123654",
            "place_id": "p-123654",
            "user_id": "u-123654",
            "text": "very beautiful",
            "created_at": "2024-02-08T12:00:00.563721",
            "updated_at": "2024-02-12T12:00:00.563721"
        }

        n_rvw = Review(**data)

        self.assertIsInstance(n_rvw, Review)
        self.assertIsInstance(n_rvw, BaseModel)
        self.assertIsInstance(n_rvw.id, str)
        self.assertIsInstance(n_rvw.created_at, datetime)
        self.assertIsInstance(n_rvw.updated_at, datetime)
        self.assertIsInstance(n_rvw.place_id, str)
        self.assertIsInstance(n_rvw.user_id, str)
        self.assertIsInstance(n_rvw.text, str)
        self.assertEqual(n_rvw.id, "r-123654")
        self.assertEqual(n_rvw.place_id, "p-123654")
        self.assertEqual(n_rvw.user_id, "u-123654")
        self.assertEqual(n_rvw.text, "very beautiful")

    def test_func_to_dict(self):
        """
            test to_dict class method
        """
        object_dict = self.rvw.to_dict()
        expect_dict = self.rvw.__dict__.copy()
        expect_dict["__class__"] = self.rvw.__class__.__name__
        expect_dict["updated_at"] = self.rvw.updated_at.isoformat()
        expect_dict["created_at"] = self.rvw.created_at.isoformat()
        self.assertDictEqual(expect_dict, object_dict)

    def test_func_save(self):
        """"
            test save class method
        """
        bf_update = self.rvw.updated_at
        self.rvw.text = "very nice"
        self.rvw.save()
        af_update = self.rvw.updated_at
        self.assertNotEqual(bf_update, af_update)

    def test_func_str(self):
        """
            test str class method
        """
        s = self.rvw.__class__.__name__
        exp_string = f"[{s}] ({self.rvw.id}) <{self.rvw.__dict__}>"
        self.assertEqual(self.rvw.__str__(), exp_string)

