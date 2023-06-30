import unittest

from models.base import Base

class TestBase(unittest.TestCase):

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string([{}]), "[{}]")
        self.assertEqual(Base.to_json_string([]), "[]")
