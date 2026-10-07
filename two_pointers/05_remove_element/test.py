"""Tests for: Remove Element

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
    (([3, 2, 2, 3], 3), [2, 2]),
    (([0, 1, 2, 2, 3, 0, 4, 2], 2), [0, 1, 3, 0, 4]),
    (([1, 2, 3], 4), [1, 2, 3]),
    (([], 1), []),
    (([1], 1), []),
    (([2, 2, 2], 2), []),
]


class Test(unittest.TestCase):
    def test_cases(self):
        for original_args, expected in CASES:
            args = copy.deepcopy(original_args)
            with self.subTest(input=original_args):
                k = sol.remove_element(*args)
                self.assertEqual(k, len(expected))
                self.assertEqual(sorted(args[0][:k]), sorted(expected))


if __name__ == "__main__":
    unittest.main()
