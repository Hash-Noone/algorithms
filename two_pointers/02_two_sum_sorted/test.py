"""Tests for: Two Sum (Sorted Array)

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
    (([2, 7, 11, 15], 9), [1, 2]),
    (([2, 3, 4], 6), [1, 3]),
    (([-1, 0], -1), [1, 2]),
    (([1, 2, 3, 4, 4, 9, 56, 90], 8), [4, 5]),
    (([0, 0, 3, 4], 0), [1, 2]),
    (([5, 25, 75], 100), [2, 3]),
    (([-5, -3, 0, 2, 8], 5), [2, 5]),
]


class Test(unittest.TestCase):
    def test_cases(self):
        for original_args, expected in CASES:
            args = copy.deepcopy(original_args)
            with self.subTest(input=original_args):
                self.assertEqual(sol.two_sum_sorted(*args), expected)


if __name__ == "__main__":
    unittest.main()
