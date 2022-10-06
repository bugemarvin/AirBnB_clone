#!/usr/bin/python3
"""Unitest for base model
"""

from models.base_model import BaseModel
import unittest
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """Test cases for the base model
    """
    def test_checking_for_docstring_BaseModel(self):
        """checking for docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_method_BaseModel(self):
        """chekcing if Basemodel have methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init_BaseModel(self):
        """test if the base is an type BaseModel"""
        self.assertTrue(isinstance(self.base, BaseModel))

    @unittest.skipIf(env.get('HBNB_TYPE_STORAGE') == 'db',
                     "dbstorage does not support BaseModel objects")
    def test_save_BaesModel(self):
        """test if the save works"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    @unittest.skipIf(env.get('HBNB_TYPE_STORAGE') != 'db',
                     "dbstorage does not support BaseModel objects")
    def test_save_BaseModeldb(self):
        """empty test for requirements"""
        pass

    def test_to_dict_BaseModel(self):
        """test if dictionary works"""
        my_base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(my_base_dict['created_at'], str)
        self.assertIsInstance(my_base_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
