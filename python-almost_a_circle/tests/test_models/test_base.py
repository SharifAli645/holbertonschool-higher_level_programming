import unittest
import json
import pep8

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
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())
        
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

        r1 = Rectangle(10, 5, 1, 12)
        r2 = Rectangle(4, 6)
        dicty = [r1.to_dictionary(), r2.to_dictionary()]
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as f:
            j_dicty = json.loads(f.read())
        self.assertTrue(dicty == j_dicty)

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
        l = Rectangle.load_from_file()
        self.assertDictEqual(l[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(type(l[0]), Rectangle)
        self.assertDictEqual(l[1].to_dictionary(), r2.to_dictionary())
        self.assertEqual(type(l[1]), Rectangle)
        self.assertTrue(type(l) == list)

        s1 = Square(6, 12, 24, 48)
        s2 = Square(7, 14, 28, 56)
        Square.save_to_file([s1, s2])
        l = Square.load_from_file()
        self.assertDictEqual(l[0].to_dictionary(), s1.to_dictionary())
        self.assertEqual(type(l[0]), Square)
        self.assertDictEqual(l[1].to_dictionary(), s2.to_dictionary())
        self.assertEqual(type(l[0]), Square)
        self.assertTrue(type(l) == list)

    def test_pep8(self):
        """checks pep 8"""
        p8 = pep8.StyleGuide(quiet=True)
        outcome = p8.check_files(['models/base.py',
                                'tests/test_models/test_base.py'])
