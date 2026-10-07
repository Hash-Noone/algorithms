# Two Pointers & Sliding Window Practice

18 coding problems to practise two classic array and string techniques. The two techniques live in **separate folders** so you never mix them up:

```
two_pointers/        9 problems + a README explaining the technique
sliding_window/      9 problems + a README explaining the technique
run_all.py           run every test and see a summary
```

Start by reading the README in the topic folder, then work through the problems in order.

## Inside each problem folder

```
01_valid_palindrome/
├── README.md              the question, examples, expected output, constraints, hint
├── solution.py            your code goes here (starts as a stub)
├── test.py                tests for your solution
```

## How to use

1. Open a problem's `README.md` and read the question.
2. Write your code in `solution.py`.
3. Run the tests from inside that folder:

```bash
cd two_pointers/01_valid_palindrome
python test.py          # test your solution
```

Or check everything at once from the repo root:

```bash
python run_all.py                  # all 18 problems
python run_all.py sliding_window   # one topic only
```

`run_all.py` marks each problem **PASS**, **FAIL** or **TODO** (not started yet).

Requires Python 3.8+. No packages to install; tests use the built-in `unittest`.

## Problems

### Two Pointers

| # | Problem | Pattern |
|---|---------|---------|
| 1 | [Valid Palindrome](two_pointers/01_valid_palindrome/) | Opposite-direction pointers |
| 2 | [Two Sum (Sorted Array)](two_pointers/02_two_sum_sorted/) | Opposite-direction pointers |
| 3 | [Container With Most Water](two_pointers/03_container_with_most_water/) | Opposite-direction pointers |
| 4 | [Remove Duplicates from Sorted Array](two_pointers/04_remove_duplicates_sorted/) | Same-direction (slow & fast) pointers |
| 5 | [Remove Element](two_pointers/05_remove_element/) | Same-direction (slow & fast) pointers |
| 6 | [Move Zeroes](two_pointers/06_move_zeroes/) | Same-direction (slow & fast) pointers |
| 7 | [3Sum](two_pointers/07_three_sum/) | Two pointers + sorting |
| 8 | [3Sum Closest](two_pointers/08_three_sum_closest/) | Two pointers + sorting |
| 9 | [4Sum](two_pointers/09_four_sum/) | Two pointers + sorting |

### Sliding Window

| # | Problem | Pattern |
|---|---------|---------|
| 1 | [Maximum Average Subarray](sliding_window/01_maximum_average_subarray/) | Fixed-size window |
| 2 | [Sub-arrays of Size K With Average At Least Threshold](sliding_window/02_subarrays_average_threshold/) | Fixed-size window |
| 3 | [Maximum Number of Vowels in a Substring](sliding_window/03_max_vowels_in_substring/) | Fixed-size window |
| 4 | [Minimum Size Subarray Sum](sliding_window/04_minimum_size_subarray_sum/) | Variable-size window |
| 5 | [Longest Substring Without Repeating Characters](sliding_window/05_longest_substring_no_repeats/) | Variable-size window |
| 6 | [Longest Repeating Character Replacement](sliding_window/06_longest_repeating_character_replacement/) | Variable-size window |
| 7 | [Permutation in String](sliding_window/07_permutation_in_string/) | Window + frequency map |
| 8 | [Find All Anagrams in a String](sliding_window/08_find_all_anagrams/) | Window + frequency map |
| 9 | [Minimum Window Substring](sliding_window/09_minimum_window_substring/) | Window + frequency map |
