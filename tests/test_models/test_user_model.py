#!/usr/bin/python3
"""
Unittest for User class model
"""
import unittest
from models.user import User
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestUserClass(unittest.TestCase):
    """
    test class for the User Class
    """
    usr = User()
    usr.email = "ahmed.gamal@gmail.com"
    usr.password = "usrahmed"
    usr.first_name = "Ahmed"
    usr.last_name = "Gamal"

    def test_defaults(self):
        """test default values"""

        usr = User()
        self.assertEqual(usr.email, "")
        self.assertEqual(usr.password, "")
        self.assertEqual(usr.first_name, "")
        self.assertEqual(usr.last_name, "")

    def test_object_without_kwargs(self):
        """
        create an object of User class without kwargs
        """
        self.assertIsInstance(self.usr, User)
        self.assertIsInstance(self.usr, BaseModel)
        self.assertIsInstance(self.usr.id, str)
        self.assertIsInstance(self.usr.created_at, datetime)
        self.assertIsInstance(self.usr.updated_at, datetime)
        self.assertIsInstance(self.usr.email, str)
        self.assertIsInstance(self.usr.password, str)
        self.assertIsInstance(self.usr.first_name, str)
        self.assertIsInstance(self.usr.last_name, str)
        self.assertEqual(self.usr.email, "ahmed.gamal@gmail.com")
        self.assertEqual(self.usr.password, "usrahmed")
        self.assertEqual(self.usr.first_name, "Ahmed")
        self.assertEqual(self.usr.last_name, "Gamal")

    def test_object_with_kwargs(self):
        """
        create an object of User class using kwargs
        """
        data = {
            "id": "u-123456",
            "email": "Nil.Ahmed@gmail.com",
            "password": "nilusrahmed",
            "first_name": "Nil",
            "last_name": "Ahmed",
            "created_at": "2024-02-08T12:00:00.563721",
            "updated_at": "2024-02-12T12:00:00.563721"
        }

        n_usr = User(**data)

        self.assertIsInstance(n_usr, User)
        self.assertIsInstance(n_usr, BaseModel)
        self.assertIsInstance(n_usr.id, str)
        self.assertIsInstance(n_usr.created_at, datetime)
        self.assertIsInstance(n_usr.updated_at, datetime)
        self.assertIsInstance(n_usr.email, str)
        self.assertIsInstance(n_usr.password, str)
        self.assertIsInstance(n_usr.first_name, str)
        self.assertIsInstance(n_usr.last_name, str)

        self.assertEqual(n_usr.id, "u-123456")
        self.assertEqual(n_usr.email, "Nil.Ahmed@gmail.com")
        self.assertEqual(n_usr.password, "nilusrahmed")
        self.assertEqual(n_usr.first_name, "Nil")
        self.assertEqual(n_usr.last_name, "Ahmed")

    def test_func_to_dict(self):
        """
            test to_dict class method
        """
        object_dict = self.usr.to_dict()
        expect_dict = self.usr.__dict__.copy()
        expect_dict["__class__"] = self.usr.__class__.__name__
        expect_dict["updated_at"] = self.usr.updated_at.isoformat()
        expect_dict["created_at"] = self.usr.created_at.isoformat()
        self.assertDictEqual(expect_dict, object_dict)

    def test_func_save(self):
        """"
            test save class method
        """
        bf_update = self.usr.updated_at
        self.usr.email = "ahmed.gamal@gmail.com"
        self.usr.save()
        af_update = self.usr.updated_at
        self.assertNotEqual(bf_update, af_update)

    def test_func_str(self):
        """
            test str class method
        """
        s = self.usr.__class__.__name__
        exp_string = f"[{s}] ({self.usr.id}) {self.usr.__dict__}"
        self.assertEqual(self.usr.__str__(), exp_string)

