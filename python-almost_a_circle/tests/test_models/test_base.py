import unittest
import json

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):

    def test_id(self):
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

        l_int = [{'id': 8, 'size': 400}]
        j_int = Square.to_json_string(l_int)
        l_out = Square.from_json_string(j_int)
        self.assertEqual(l_int, l_out)

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

