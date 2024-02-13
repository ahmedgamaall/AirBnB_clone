#!/usr/bin/python3
"""
test File Storage
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os

class TestFileStorage(unittest.TestCase):
    """
    test File Storage class
    """
    file_storing = FileStorage()

    def test_defaults(self):
        """test default values"""
        init_counter = len(self.file_storing.all())
        odict = self.file_storing.all().copy()
        n_bs = BaseModel()
        
        self.file_storing.new(n_bs)
        self.file_storing.save()
        self.file_storing.reload()
        
        update_counter = len(self.file_storing.all())
        self.assertEqual(update_counter, init_counter + 1)
        
        objectk = f"BaseModel.{n_bs.id}"
        self.assertIn(objectk, self.file_storing.all())
        
        objectr = self.file_storing.all()[objectk]
        self.assertEqual(objectr.updated_at, n_bs.updated_at)

        os.remove("file.json")
        n_bs = BaseModel()
        n_bs.save()
        self.assertTrue(os.path.exists("file.json"))