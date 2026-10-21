"""Tests for: Longest Substring Without Repeating Characters

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
    (('abcabcbb',), 3),
    (('bbbbb',), 1),
    (('pwwkew',), 3),
    (('',), 0),
    ((' ',), 1),
    (('abba',), 2),
    (('dvdf',), 3),
    (('tmmzuxt',), 5),
]


class Test(unittest.TestCase):
    def test_cases(self):
        for original_args, expected in CASES:
            args = copy.deepcopy(original_args)
            with self.subTest(input=original_args):
                self.assertEqual(sol.length_of_longest_substring(*args), expected)


if __name__ == "__main__":
    unittest.main()
