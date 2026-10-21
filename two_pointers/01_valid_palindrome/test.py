"""Tests for: Valid Palindrome

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
    (('A man, a plan, a canal: Panama',), True),
    (('race a car',), False),
    ((' ',), True),
    (('',), True),
    (('0P',), False),
    (('ab_a',), True),
    (('.,',), True),
    (('Was it a car or a cat I saw?',), True),
    (('abca',), False),
]


class Test(unittest.TestCase):
    def test_cases(self):
        for original_args, expected in CASES:
            args = copy.deepcopy(original_args)
            with self.subTest(input=original_args):
                self.assertEqual(sol.valid_palindrome(*args), expected)


if __name__ == "__main__":
    unittest.main()
