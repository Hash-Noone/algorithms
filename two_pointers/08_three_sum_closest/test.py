"""Tests for: 3Sum Closest

    python test.py          # test your solution.py
"""
import copy
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import solution as sol

# (arguments, expected result)
CASES = [
    (([-1, 2, 1, -4], 1), 2),
    (([0, 0, 0], 1), 0),
    (([1, 1, 1, 0], -100), 2),
    (([1, 1, -1, -1, 3], -1), -1),
    (([4, 0, 5, -5, 3, 3, 0, -4, -5], -2), -2),
    (([10, 20, 30, 40], 100), 90),
]


class Test(unittest.TestCase):
    def test_cases(self):
        for original_args, expected in CASES:
            args = copy.deepcopy(original_args)
            with self.subTest(input=original_args):
                self.assertEqual(sol.three_sum_closest(*args), expected)


if __name__ == "__main__":
    unittest.main()
