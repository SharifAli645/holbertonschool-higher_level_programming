#!/usr/bin/python3


from unittest import TestCase, mock
from io import StringIO
import json
import pycodestyle
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(TestCase):
    """Class test Rectangle"""

    def test_basic(self):
        self.assertRaises(TypeError, Rectangle, None)
        self.assertRaises(TypeError, Rectangle, 1)
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, 4, 5, 6)

        Base._Base__nb_objects = 0
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

    def test_area(self):
        self.assertEqual(Rectangle(2, 4).area(), 8)
        self.assertEqual(Rectangle(10, 10).area(), 100)

    def test_display(self):
        with mock.patch('sys.stdout', new=StringIO()) as output:
            Rectangle(3, 2).display()
            self.assertEqual(output.getvalue(), '###\n###\n')

        with mock.patch('sys.stdout', new=StringIO()) as output:
            Rectangle(3, 2, 3, 3).display()
            self.assertEqual(output.getvalue(), '\n\n\n   ###\n   ###\n')

    def test_str(self):
        Base._Base__nb_objects = 0
        r1 = Rectangle(4, 8, 16, 32, 64)
        r2 = Rectangle(5, 5)
        
        s1 = r1.__str__()
        s2 = r2.__str__()
        self.assertEqual(s1, "[Rectangle] (64) 16/32 - 4/8")
        self.assertEqual(s2, "[Rectangle] (1) 0/0 - 5/5") 
