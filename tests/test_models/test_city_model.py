#!/usr/bin/python3
"""
Unittest for City model
"""
import unittest
from models.city import City
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestCityClass(unittest.TestCase):
    """
    test class for the City Class
    """
    cy = City()
    cy.name = "Qena"
    cy.id = "695-654-789"

    def test_defaults(self):
        """test default value"""

        cty = City()
        self.assertEqual(cty.name, "")
        self.assertEqual(cty.state_id, "")

    def test_object_without_kwargs(self):
        """
        create an object of City class without kwargs
        """
        self.assertIsInstance(self.cy, City)
        self.assertIsInstance(self.cy, BaseModel)
        self.assertIsInstance(self.cy.id, str)
        self.assertIsInstance(self.cy.name, str)
        self.assertIsInstance(self.cy.created_at, datetime)
        self.assertIsInstance(self.cy.updated_at, datetime)
        self.assertEqual(self.cy.name, "Qena")
        self.assertEqual(self.cy.id, "695-654-789")

    def test_object_with_kwargs(self):
        """
        create an object of City class using kwargs
        """
        cy_json = self.cy.to_dict()
        n_cy = City(**cy_json)
        self.assertIsInstance(n_cy, City)
        self.assertIsInstance(n_cy.id, str)
        self.assertIsInstance(n_cy.created_at, datetime)
        self.assertIsInstance(n_cy.updated_at, datetime)
        self.assertEqual(n_cy.name, "Qena")
        self.assertEqual(n_cy.id, "695-654-789")
        self.assertNotEqual(n_cy, self.cy)
        self.assertDictEqual(n_cy.__dict__, self.cy.__dict__)
        n_cy.state_id = "456-987"
        n_cy.name = "Qenaa"
        n_cy.save()
        self.assertEqual(n_cy.state_id, "456-987")
        self.assertEqual(n_cy.name, "Qenaa")
        self.assertEqual(n_cy.__dict__["name"], "Qenaa")
        self.assertEqual(n_cy.__dict__["state_id"], "456-987")

    def test_func_to_dict(self):
        """
            test to_dict class method
        """
        object_dict = self.cy.to_dict()
        expected_dic = self.cy.__dict__.copy()
        expected_dic["__class__"] = self.cy.__class__.__name__
        expected_dic["updated_at"] = self.cy.updated_at.isoformat()
        expected_dic["created_at"] = self.cy.created_at.isoformat()
        self.assertDictEqual(expected_dic, object_dict)

    def test_func_save(self):
        """"
            test save class method
        """
        bf_update = self.cy.updated_at
        self.cy.name = "Qena"
        self.cy.save()
        af_update = self.cy.updated_at
        self.assertNotEqual(bf_update, af_update)

    def test_func_str(self):
        """
            test str class method
        """
        s = self.cy.__class__.__name__
        exp_string = f"[{s}] ({self.cy.id}) {self.cy.__dict__}"
        self.assertEqual(self.cy.__str__(), exp_string)