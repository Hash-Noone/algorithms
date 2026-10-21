"""Tests for: Maximum Average Subarray

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
    (([1, 12, -5, -6, 50, 3], 4), 12.75),
    (([5], 1), 5.0),
    (([-1], 1), -1.0),
    (([0, 4, 0, 3, 2], 1), 4.0),
    (([-5, -3, -8], 2), -4.0),
]


class Test(unittest.TestCase):
    def test_cases(self):
        for original_args, expected in CASES:
            args = copy.deepcopy(original_args)
            with self.subTest(input=original_args):
                self.assertAlmostEqual(sol.find_max_average(*args), expected, places=5)


if __name__ == "__main__":
    unittest.main()
