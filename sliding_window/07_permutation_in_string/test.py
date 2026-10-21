"""Tests for: Permutation in String

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
    (('ab', 'eidbaooo'), True),
    (('ab', 'eidboaoo'), False),
    (('a', 'a'), True),
    (('abc', 'ab'), False),
    (('adc', 'dcda'), True),
    (('hello', 'ooolleoooleh'), False),
]


class Test(unittest.TestCase):
    def test_cases(self):
        for original_args, expected in CASES:
            args = copy.deepcopy(original_args)
            with self.subTest(input=original_args):
                self.assertEqual(sol.check_inclusion(*args), expected)


if __name__ == "__main__":
    unittest.main()
