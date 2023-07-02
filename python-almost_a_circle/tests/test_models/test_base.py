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
