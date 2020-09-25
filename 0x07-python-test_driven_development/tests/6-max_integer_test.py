#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_file_doc(self):
        docs = __import__('6-max_integer').__doc__
        self.assertTrue(len(docs) > 1)

    def test_func_doc(self):
        docs = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(len(docs) > 1)

    def test_safe(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1, 2, 3.99, 4]), 4)
        self.assertEqual(max_integer([[0, 1, 2], [3, 4, 5]]), [3, 4, 5])
        self.assertEqual(max_integer("abcd"), "d")
        self.assertEqual(max_integer(), None)

    def test_fail(self):
        with self.assertRaises(TypeError):
            max_integer({1, 2, 3}, {4, 5, 6})
        with self.assertRaises(TypeError):
            max_integer([None, 44])
        with self.assertRaises(TypeError):
            max_integer(None)
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3], [4, 5, 6])

if __name__ == "__main__":
    unittest.main()
