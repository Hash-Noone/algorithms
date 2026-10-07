"""Tests for: Longest Repeating Character Replacement

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
    (('ABAB', 2), 4),
    (('AABABBA', 1), 4),
    (('A', 0), 1),
    (('ABC', 0), 1),
    (('AAAA', 2), 4),
    (('ABBB', 2), 4),
    (('ABCDE', 1), 2),
]


class Test(unittest.TestCase):
    def test_cases(self):
        for original_args, expected in CASES:
            args = copy.deepcopy(original_args)
            with self.subTest(input=original_args):
                self.assertEqual(sol.character_replacement(*args), expected)


if __name__ == "__main__":
    unittest.main()
