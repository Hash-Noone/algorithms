"""Tests for: Sub-arrays of Size K With Average At Least Threshold

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
    (([2, 2, 2, 2, 5, 5, 5, 8], 3, 4), 3),
    (([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5), 6),
    (([1], 1, 1), 1),
    (([1, 1, 1], 2, 2), 0),
    (([5, 5, 5], 3, 5), 1),
    (([4, 4, 4, 4], 1, 4), 4),
]


class Test(unittest.TestCase):
    def test_cases(self):
        for original_args, expected in CASES:
            args = copy.deepcopy(original_args)
            with self.subTest(input=original_args):
                self.assertEqual(sol.count_subarrays(*args), expected)


if __name__ == "__main__":
    unittest.main()
