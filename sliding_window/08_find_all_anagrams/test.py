"""Tests for: Find All Anagrams in a String

    python test.py          # test your solution.py
    python test.py --ref    # test reference_solution.py
"""
import copy
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if "--ref" in sys.argv:
    sys.argv.remove("--ref")
    import reference_solution as sol
else:
    import solution as sol

# (arguments, expected result)
CASES = [
    (('cbaebabacd', 'abc'), [0, 6]),
    (('abab', 'ab'), [0, 1, 2]),
    (('a', 'ab'), []),
    (('baa', 'aa'), [1]),
    (('aaaaaaaaaa', 'aaaaaaaaaaaaa'), []),
    (('abacbabc', 'abc'), [1, 2, 3, 5]),
]


class Test(unittest.TestCase):
    def test_cases(self):
        for original_args, expected in CASES:
            args = copy.deepcopy(original_args)
            with self.subTest(input=original_args):
                self.assertEqual(sorted(sol.find_anagrams(*args)), expected)


if __name__ == "__main__":
    unittest.main()
