#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test class"""
    def test_empty_list(self):
        """Testcase for None"""
        self.assertEqual(max_integer([]), None)

    def test_max_int(self):
        """Testcase for normal scenario"""
        self.assertEqual(max_integer([1, 2, 5, 3, 4]), 5)

    def test_equal(self):
        """Testcase for equal elements"""
        self.assertEqual(max_integer([2,2,2,2]), 2)

    def test_one_element(self):
        """Testcase for one element"""
        self.assertEqual(max_integer([40]), 40)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1,-2,-85,-10]), -1)

    def test_big_numbers(self):
        temp_list = list(range(1000000))
        self.assertEqual(max_integer(temp_list), 999999)

    def test_floats(self):
        self.assertEqual(max_integer([0.25, 0.45, 0.10, 0.4]), 0.45)

    def test_negative_floats(self):
        self.assertEqual(max_integer([-0.25, -0.45, -0.10, -0.4]), -0.1)

if __name__ == '__main__':
    unittest.main()
