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

if __name__ == '__main__':
    unittest.main()
