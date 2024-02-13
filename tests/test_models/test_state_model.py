#!/usr/bin/python3
"""
Unittest for State Class
"""
import unittest
from models.state import State
from models.base_model import BaseModel
from datetime import datetime
from models import storage

class TestStateClass(unittest.TestCase):
    """
    test class for the State Class
    """
    st = State()
    st.name = "good"

    def test_defaults(self):
        """test default values"""

        s = State()
        self.assertEqual(s.name, "")

    def test_object_without_kwargs(self):
        """
        create an object of State class without kwargs
        """
        self.assertIsInstance(self.st, State)
        self.assertIsInstance(self.st, BaseModel)
        self.assertIsInstance(self.st.id, str)
        self.assertIsInstance(self.st.created_at, datetime)
        self.assertIsInstance(self.st.updated_at, datetime)
        self.assertIsInstance(self.st.name, str)
        self.assertEqual(self.st.name, "good")

    def test_object_with_kwargs(self):
        """
        create an object of State class using kwargs
        """
        data = {
            "id": "654-123",
            "name": "Nice",
            "created_at": "2024-02-08T12:00:00.563721",
            "updated_at": "2024-02-12T12:00:00.563721"
        }

        n_st = State(**data)

        self.assertIsInstance(n_st, State)
        self.assertIsInstance(n_st, BaseModel)
        self.assertIsInstance(n_st.id, str)
        self.assertIsInstance(n_st.created_at, datetime)
        self.assertIsInstance(n_st.updated_at, datetime)
        self.assertIsInstance(n_st.name, str)
        
        self.assertEqual(n_st.id, "654-123")
        self.assertEqual(n_st.name, "Nice")

    def test_func_to_dict(self):
        """
            test to_dict class method
        """
        object_dict = self.st.to_dict()
        expect_dict = self.st.__dict__.copy()
        expect_dict["__class__"] = self.st.__class__.__name__
        expect_dict["updated_at"] = self.st.updated_at.isoformat()
        expect_dict["created_at"] = self.st.created_at.isoformat()
        self.assertDictEqual(expect_dict, object_dict)

    def test_func_save(self):
        """"
            test save class method
        """
        bf_update = self.st.updated_at
        self.st.name = "good"
        self.st.save()
        af_update = self.st.updated_at
        self.assertNotEqual(bf_update, af_update)

    def test_func_str(self):
        """
            test str class method
        """
        s = self.st.__class__.__name__
        exp_string = f"[{s}] ({self.st.id}) {self.st.__dict__}"
        self.assertEqual(self.st.__str__(), exp_string)