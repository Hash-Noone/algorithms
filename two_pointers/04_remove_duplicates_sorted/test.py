"""Tests for: Remove Duplicates from Sorted Array

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
    (([1, 1, 2],), [1, 2]),
    (([0, 0, 1, 1, 1, 2, 2, 3, 3, 4],), [0, 1, 2, 3, 4]),
    (([1, 2, 3],), [1, 2, 3]),
    (([],), []),
    (([5, 5, 5],), [5]),
    (([-3, -3, -1, 0, 0],), [-3, -1, 0]),
]


class Test(unittest.TestCase):
    def test_cases(self):
        for original_args, expected in CASES:
            args = copy.deepcopy(original_args)
            with self.subTest(input=original_args):
                k = sol.remove_duplicates(*args)
                self.assertEqual(k, len(expected))
                self.assertEqual(args[0][:k], expected)


if __name__ == "__main__":
    unittest.main()
