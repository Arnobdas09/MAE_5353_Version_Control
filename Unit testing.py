# -*- coding: utf-8 -*-
"""
Arnob Das
MAE 5353
Module F HW#1
Unit Testing

____Implement a unit test of your choice (pytest, unittest, doctest) to the code shown below
def func(x):
    return x + 1______

Created on Sun Apr 14 02:26:08 2024

@author: arnob
"""

import unittest
def func(x):
    return x + 1

class TestFunction(unittest.TestCase):

  def test_add_one(self):
    """
    This test verifies that the function func(x) adds 1 to the input value.
    """
    # Test with positive input
    result = func(5)
    self.assertEqual(result, 6)

    # Test with negative input
    result = func(-2)
    self.assertEqual(result, -1)

    # Test with zero input
    result = func(0)
    self.assertEqual(result, 1)

if __name__ == "__main__":
  unittest.main()
