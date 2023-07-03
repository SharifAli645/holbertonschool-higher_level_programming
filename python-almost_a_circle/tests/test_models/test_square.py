#!/usr/bin/python3


from unittest import TestCase
import json
import pycodestyle
from models.base import Base
from models.square import Square


class TestSquare(TestCase):
    """Class test Square"""

    def test_basic(self):
        self.assertRaises(TypeError, Square, None)
        self.assertRaises(TypeError, Square, 1, 2, 3, 4, 5, 6)

        Base._Base__nb_objects = 0
        self.assertEqual(Square(2, 4).id, 1)
        self.assertEqual(Square(3, 6).id, 2)

        self.assertEqual(Square(2, 4, 6, 12).id, 12)
        self.assertEqual(Square(3, 6, 12, 24).id, 24)

        Base._Base__nb_objects = 0
        r = Square(10, 20, 30)
        r.size = 11
        self.assertEqual(r.size, 11)
        r.x = 21
        self.assertEqual(r.x, 21)
        r.y = 31
        self.assertEqual(r.y, 31)

    def test_values(self):
        Base._Base__nb_objects = 0
        self.assertRaises(ValueError, Square, -2)
        self.assertRaises(ValueError, Square, 2, -2)
        self.assertRaises(ValueError, Square, 2, 2, -3)
        self.assertRaises(ValueError, Square, 0)

    def test_types(self):
        self.assertRaises(TypeError, Square, "2")
        self.assertRaises(TypeError, Square, 2, "2")
        self.assertRaises(TypeError, Square, 2, 2, "2")
        self.assertRaises(TypeError, Square, 2, 2, 2, 2, 2)

    def test_str(self):
        Base._Base__nb_objects = 0
        r1 = Square(4, 8, 16, 32)
        r2 = Square(5)
        
        s1 = r1.__str__()
        s2 = r2.__str__()
        self.assertEqual(s1, "[Square] (32) 8/16 - 4")
        self.assertEqual(s2, "[Square] (1) 0/0 - 5") 
