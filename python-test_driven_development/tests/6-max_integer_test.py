#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test class for max_integer function"""

    def test_empty_list(self):
        """Test with empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test with one element"""
        self.assertEqual(max_integer([5]), 5)

    def test_multiple_integers(self):
        """Test with normal list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        """Test with negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test with positive and negative integers"""
        self.assertEqual(max_integer([-10, 5, 3, -1]), 5)

    def test_same_numbers(self):
        """Test list with same numbers"""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_max_at_beginning(self):
        """Test when max is first element"""
        self.assertEqual(max_integer([10, 2, 3, 4]), 10)

    def test_max_at_end(self):
        """Test when max is last element"""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)

    def test_float_numbers(self):
        """Test with float numbers"""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_mixed_int_float(self):
        """Test mixed int and float"""
        self.assertEqual(max_integer([1, 2.5, 3, 0]), 3)


if __name__ == '__main__':
    unittest.main()
