"""Tests for: Container With Most Water

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
    (([1, 8, 6, 2, 5, 4, 8, 3, 7],), 49),
    (([1, 1],), 1),
    (([4, 3, 2, 1, 4],), 16),
    (([1, 2, 1],), 2),
    (([0, 0, 0],), 0),
    (([2, 3, 4, 5, 18, 17, 6],), 17),
]


class Test(unittest.TestCase):
    def test_cases(self):
        for original_args, expected in CASES:
            args = copy.deepcopy(original_args)
            with self.subTest(input=original_args):
                self.assertEqual(sol.max_area(*args), expected)


if __name__ == "__main__":
    unittest.main()
