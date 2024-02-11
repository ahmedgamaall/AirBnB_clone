#!/usr/bin/python3
"""
Unittest for BaseModel
"""
import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestBaseModelClass(unittest.TestCase):
    """
    test class for BaseModel Class
    """
    bsmodel = BaseModel()
    bsmodel.name = "Father for all classes"
    bsmodel.my_number = 95

    def test_object_without_kwargs(self):
        """
        create an object of BaseModel class without kwargs
        """
        self.assertIsInstance(self.bsmodel, BaseModel)
        self.assertIsInstance(self.bsmodel.id, str)
        self.assertIsInstance(self.bsmodel.created_at, datetime)
        self.assertIsInstance(self.bsmodel.updated_at, datetime)
        self.assertEqual(self.bsmodel.name, "Father for all classes")
        self.assertEqual(self.bsmodel.my_number, 95)

    def test_object_with_kwargs(self):
        """
        create an object of BaseModel class without kwargs
        """
        bs_json = self.bsmodel.to_dict()
        n_bs = BaseModel(**bs_json)
        self.assertIsInstance(n_bs, BaseModel)
        self.assertIsInstance(n_bs.id, str)
        self.assertIsInstance(n_bs.created_at, datetime)
        self.assertIsInstance(n_bs.updated_at, datetime)
        self.assertEqual(n_bs.name, "My First Model")
        self.assertEqual(n_bs.my_number, 59)
        self.assertNotEqual(n_bs, self.bsmodel)
        self.assertDictEqual(n_bs.__dict__, self.bsmodel.__dict__)

    def test_func_to_dict(self):
        """
            test to_dict class method
        """
        object_dict = self.bsmodel.to_dict()
        expect_dict = self.bsmodel.__dict__.copy()
        expect_dict["__class__"] = self.bsmodel.__class__.__name__
        expect_dict["updated_at"] = self.bsmodel.updated_at.isoformat()
        expect_dict["created_at"] = self.bsmodel.created_at.isoformat()
        self.assertDictEqual(expect_dict, object_dict)

    def test_func_save(self):
        """"
            test save class method
        """
        bf_update = self.bsmodel.updated_at
        self.bsmodel.my_number = 97
        self.bsmodel.save()
        af_update = self.bsmodel.updated_at
        self.assertNotEqual(bf_update, af_update)

    def test_func_str(self):
        """
            test str class method
        """
        s = self.bsmodel.__class__.__name__
        exp_string = f"[{s}] ({self.bsmodel.id}) <{self.bsmodel.__dict__}>"
        self.assertEqual(self.bsmodel.__str__(), exp_string)

