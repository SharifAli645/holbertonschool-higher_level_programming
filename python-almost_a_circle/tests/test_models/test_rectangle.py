import unittest
import json
import pep8

from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """"""
    def test_basic(self):
        self.assertRaises(TypeError, Rectangle, None)
        self.assertRaises(TypeError, Rectangle, 1)
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, 4, 5, 6)

        self.assertEqual(Rectangle(2, 4).id, 1)
        self.assertEqual(Rectangle(3, 6).id, 2)

        self.assertEqual(Rectangle(2, 4, 6, 12, 24).id, 24)
        self.assertEqual(Rectangle(3, 6, 12, 24, 42).id, 42)

        Base._Base__nb_objects = 0
        r = Rectangle(10, 20, 30, 40)
        r.width = 11
        self.assertEqual(r.width, 11)
        r.height = 21
        self.assertEqual(r.height, 21)
        r.x = 31
        self.assertEqual(r.x, 31)
        r.y = 41
        self.assertEqual(r.y, 41)

    def test_values(self):
        Base._Base__nb_objects = 0
        r = Rectangle(20, 20)
        self.assertRaises(ValueError, Rectangle, -2, 2)
        self.assertRaises(ValueError, Rectangle, 0, 2)
        self.assertRaises(ValueError, Rectangle, 2, 2, -3, 2)

    def test_types(self):
        self.assertRaises(TypeError, Rectangle, "2", 2)
        self.assertRaises(TypeError, Rectangle, 2, "2")
        self.assertRaises(TypeError, Rectangle, 2, 2, "2", 2)
        self.assertRaises(TypeError, Rectangle, 2, 2, 2, "2")

    def test_pep8(self):
        """checks pep 8"""
        p8 = pep8.StyleGuide(quiet=True)
        outcome = p8.check_files(['tests/test_models/test_rectangle.py']) 
