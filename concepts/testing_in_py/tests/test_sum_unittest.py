import unittest
import os
import sys
from fractions import Fraction

path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../../..")
sys.path.append(path)

from concepts.testing_in_py.my_sum import do_sum

"""
Couple of ways to run below cases:

From terminal:
a) python test_sum_unittest.py
b) python -m unittest -v test_sum_unittest.py (Here -v stands for verbose and will print result of case along with
name of the test case)
"""


class TestSum(unittest.TestCase):
    def test_sum_set(self):
        self.assertEqual(do_sum({1, 2, 3}), 6, msg="Sum should be 6")

    def test_sum_string_negative(self):
        with self.assertRaises(TypeError):
            do_sum({"Hello", "World"})

    def test_sum_fractions(self):
        fractions = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = do_sum(fractions)
        self.assertEqual(result, 1, "Should be 1")  # demonstrates a failing test


if __name__ == "__main__":
    unittest.main()
