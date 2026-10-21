"""Tests for: 4Sum

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
    (([1, 0, -1, 0, -2, 2], 0), [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
    (([2, 2, 2, 2, 2], 8), [[2, 2, 2, 2]]),
    (([], 0), []),
    (([1, 2, 3], 6), []),
    (([0, 0, 0, 0], 0), [[0, 0, 0, 0]]),
    (([-3, -1, 0, 2, 4, 5], 2), [[-3, -1, 2, 4]]),
]


class Test(unittest.TestCase):
    def test_cases(self):
        for original_args, expected in CASES:
            args = copy.deepcopy(original_args)
            with self.subTest(input=original_args):
                result = sol.four_sum(*args)
                self.assertEqual(sorted(sorted(t) for t in result), sorted(sorted(t) for t in expected))


if __name__ == "__main__":
    unittest.main()
