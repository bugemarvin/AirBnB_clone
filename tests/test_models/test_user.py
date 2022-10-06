#!/usr/bin/python3
"""
Unitest for user model
"""

from models.user import User
from time import sleep
import unittest


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the user class
    """
    def test_attributes(self):
        """Testing user attributes"""
        m = User()
        self.assertIsInstance(m.email, str)
        self.assertIsInstance(m.password, str)
        self.assertIsInstance(m.first_name, str)
        self.assertIsInstance(m.last_name, str)

    def test_addedattributes(self):
        """Testing added attributes"""
        m = User()
        m.middle_name = "Mweru"
        m.age = 50
        self.assertEqual("Mweru", m.middle_name)
        self.assertEqual(50, m.age)

    def test_todict(self):
        """testing dict keys"""
        m = User()
        dict_m = m.to_dict()
        self.assertIn('created_at', dict_m)
        self.assertIn('updated_at', dict_m)
        self.assertIn('id', dict_m)


if __name__ == "__main__":
    unittest.main()
