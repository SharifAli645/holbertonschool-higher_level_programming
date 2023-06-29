import unittest

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_width(self):
        r_1 = Rectangle(1, 1)
        r_2 = Rectangle(2, 3)
        r_3 = Rectangle(4, 4)

        self.assertEqual(r_1.width, 1)
        self.assertEqual(r_2.width, 2)
        self.assertEqual(r_3.width, 4)

    def test_height(self):
        r_1 = Rectangle(1, 1)
        r_2 = Rectangle(2, 3)
        r_3 = Rectangle(4, 4)

        self.assertEqual(r_1.height, 1)
        self.assertEqual(r_2.height, 3)
        self.assertEqual(r_3.height, 4)

    def test_x(self):
        r_1 = Rectangle(1, 1)
        r_2 = Rectangle(2, 3)
        r_3 = Rectangle(4, 4)

        self.assertEqual(r_1.x, 0)
        self.assertEqual(r_2.x, 0)
        self.assertEqual(r_3.x, 0)

    def test_y(self):
        r_1 = Rectangle(1, 1)
        r_2 = Rectangle(2, 3)
        r_3 = Rectangle(4, 4)

        self.assertEqual(r_1.y, 0)
        self.assertEqual(r_2.y, 0)
        self.assertEqual(r_3.y, 0)

    def test_area(self):
        r_1 = Rectangle(1, 1)
        r_2 = Rectangle(2, 3)
        r_3 = Rectangle(4, 4)

        self.assertEqual(r_1.area(), 1)
        self.assertEqual(r_2.area(), 6)
        self.assertEqual(r_3.area(), 16)
