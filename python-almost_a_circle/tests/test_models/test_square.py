import unittest

from models.square import Square


class TestSquare(unittest.TestCase):

    def test_size(self):
        r_1 = Square(1)
        r_2 = Square(2)
        r_3 = Square(4)
        self.assertEqual(r_1.size, 1)
        self.assertEqual(r_2.size, 2)
        self.assertEqual(r_3.size, 4)

    def test_x(self):
        r_1 = Square(1)
        r_2 = Square(2)
        r_3 = Square(4)
        self.assertEqual(r_1.x, 0)
        self.assertEqual(r_2.x, 0)
        self.assertEqual(r_3.x, 0)

    def test_y(self):
        r_1 = Square(1)
        r_2 = Square(2)
        r_3 = Square(4)
        self.assertEqual(r_1.y, 0)
        self.assertEqual(r_2.y, 0)
        self.assertEqual(r_3.y, 0)

    def test_area(self):
        r_1 = Square(1)
        r_2 = Square(2)
        r_3 = Square(4)
        self.assertEqual(r_1.area(), 1)
        self.assertEqual(r_2.area(), 4)
        self.assertEqual(r_3.area(), 16)
