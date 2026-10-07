"""Tests for: Move Zeroes

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
    (([0, 1, 0, 3, 12],), [1, 3, 12, 0, 0]),
    (([0],), [0]),
    (([1, 2, 3],), [1, 2, 3]),
    (([],), []),
    (([0, 0, 1],), [1, 0, 0]),
    (([0, 0, 0],), [0, 0, 0]),
    (([4, 0, 5, 0, 0, 6],), [4, 5, 6, 0, 0, 0]),
]


class Test(unittest.TestCase):
    def test_cases(self):
        for original_args, expected in CASES:
            args = copy.deepcopy(original_args)
            with self.subTest(input=original_args):
                result = sol.move_zeroes(*args)
                self.assertIsNone(result, "modify the list in place and return nothing")
                self.assertEqual(args[0], expected)


if __name__ == "__main__":
    unittest.main()
