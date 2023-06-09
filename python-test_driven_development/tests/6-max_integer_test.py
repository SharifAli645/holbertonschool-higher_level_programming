#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertAlmostEqual(max_integer([1, 2, 3]), 3)
        self.assertAlmostEqual(max_integer([45, 689, -156]), 689)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([-999, -1, -440, -10]), -1)
        self.assertAlmostEqual(max_integer([-9.5, 82.6, 97.96, 97.97]), 97.97)
        self.assertAlmostEqual(max_integer([True, False]), True)
        self.assertAlmostEqual(max_integer(), None)
        self.assertAlmostEqual(max_integer((4, 5, 5)), 5)
        self.assertAlmostEqual(max_integer([9]), 9)
        self.assertAlmostEqual(max_integer([-9]), -9)

    def test_values(self):
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer, [1, None, 4])
        self.assertRaises(TypeError, max_integer, {4, 5, 5})
