"""Tests for: Minimum Window Substring

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
    (('ADOBECODEBANC', 'ABC'), 'BANC'),
    (('a', 'a'), 'a'),
    (('a', 'aa'), ''),
    (('ab', 'b'), 'b'),
    (('aa', 'aa'), 'aa'),
    (('ab', 'a'), 'a'),
    (('bba', 'ab'), 'ba'),
    (('cabwefgewcwaefgcf', 'cae'), 'cwae'),
]


class Test(unittest.TestCase):
    def test_cases(self):
        for original_args, expected in CASES:
            args = copy.deepcopy(original_args)
            with self.subTest(input=original_args):
                self.assertEqual(sol.min_window(*args), expected)


if __name__ == "__main__":
    unittest.main()
