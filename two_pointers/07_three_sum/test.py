"""Tests for: 3Sum

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
    (([-1, 0, 1, 2, -1, -4],), [[-1, -1, 2], [-1, 0, 1]]),
    (([0, 1, 1],), []),
    (([0, 0, 0],), [[0, 0, 0]]),
    (([0, 0, 0, 0],), [[0, 0, 0]]),
    (([-2, 0, 1, 1, 2],), [[-2, 0, 2], [-2, 1, 1]]),
    (([],), []),
    (([1, 2, -2, -1],), []),
]


class Test(unittest.TestCase):
    def test_cases(self):
        for original_args, expected in CASES:
            args = copy.deepcopy(original_args)
            with self.subTest(input=original_args):
                result = sol.three_sum(*args)
                self.assertEqual(sorted(sorted(t) for t in result), sorted(sorted(t) for t in expected))


if __name__ == "__main__":
    unittest.main()
