#!/usr/bin/python3
"""
"""


import unittest
import json
import pycodestyle

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_id(self):
        Base._Base__nb_objects = 0
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base(6).id, 6)
        self.assertEqual(Base(-6).id, -6)
        self.assertEqual(Base(None).id, 2)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string([{}]), "[{}]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")
        j_str = json.dumps([{'width': 4, 'height': 5}])
        self.assertEqual(Base.to_json_string([{'width': 4,
                                             'height': 5}]), j_str)

    def test_save_to_file(self):
        """Test for this method"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertAlmostEqual(f.readline(), '[]')
        r3 = Rectangle(10, 7, 2, 8)
        r4 = Rectangle(2, 4)
        Rectangle.save_to_file([r3, r4])
        fi1 = r3.to_dictionary()
        fi2 = r4.to_dictionary()
        filec = [fi1, fi2]
        fi3 = Rectangle.to_json_string(filec)
        with open("Rectangle.json", "r") as f:
            self.assertAlmostEqual(f.readline(), fi3)
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertAlmostEqual(f.readline(), '[]')
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertAlmostEqual(f.readline(), '[]')
        s3 = Square(4, 2, 7)
        s4 = Square(5)
        Square.save_to_file([s3, s4])
        ss1 = s3.to_dictionary()
        ss2 = s4.to_dictionary()
        s3 = Square.to_json_string([ss1, ss2])
        with open("Square.json", "r") as f:
            self.assertAlmostEqual(f.readline(), s3)
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertAlmostEqual(f.readline(), '[]')

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string('[]'), [])

        l_int = [{'id': 8, 'width': 100, 'height': 400}]
        j_int = Rectangle.to_json_string(l_int)
        l_out = Rectangle.from_json_string(j_int)
        self.assertEqual(l_int, l_out)
        self.assertAlmostEqual(list, type(l_out))

        l_int = [{'id': 8, 'size': 400}]
        j_int = Square.to_json_string(l_int)
        l_out = Square.from_json_string(j_int)
        self.assertEqual(l_int, l_out)
        self.assertAlmostEqual(list, type(l_out))

        l_int = [
                {'id': 8, 'width': 100, 'height': 400},
                {'id': 7, 'width': 10, 'height': 40}
                ]
        j_int = Rectangle.to_json_string(l_int)
        l_out = Rectangle.from_json_string(j_int)
        self.assertEqual(l_int, l_out)

        l_int = [
                {'id': 8, 'size': 400},
                {'id': 7, 'size': 40}
                ]
        j_int = Square.to_json_string(l_int)
        l_out = Square.from_json_string(j_int)
        self.assertEqual(l_int, l_out)

    def test_create(self):
        dicty = {'width': 1, 'height': 3, 'x': 2, 'y': 2, 'id': 66}
        r = Rectangle.create(**dicty)
        self.assertDictEqual(r.to_dictionary(), dicty)

        dicty = {'size': 3, 'x': 2, 'y': 2, 'id': 67}
        s = Square.create(**dicty)
        self.assertDictEqual(s.to_dictionary(), dicty)

    def test_load_from_file(self):
        r1 = Rectangle(4, 8, 16, 32, 64)
        r2 = Rectangle(3, 6, 12, 24, 42)
        Rectangle.save_to_file([r1, r2])
        ls = Rectangle.load_from_file()
        self.assertDictEqual(ls[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(type(ls[0]), Rectangle)
        self.assertDictEqual(ls[1].to_dictionary(), r2.to_dictionary())
        self.assertEqual(type(ls[1]), Rectangle)
        self.assertTrue(type(ls) == list)

        s1 = Square(6, 12, 24, 48)
        s2 = Square(7, 14, 28, 56)
        Square.save_to_file([s1, s2])
        ls = Square.load_from_file()
        self.assertDictEqual(ls[0].to_dictionary(), s1.to_dictionary())
        self.assertEqual(type(ls[0]), Square)
        self.assertDictEqual(ls[1].to_dictionary(), s2.to_dictionary())
        self.assertEqual(type(ls[0]), Square)
        self.assertTrue(type(ls) == list)

    def test_pep8(self):
        """checks pep 8"""
        p8 = pycodestyle.StyleGuide(quiet=True)
        outcome = p8.check_files(['models/base.py',
                                 'tests/test_models/test_base.py'])
