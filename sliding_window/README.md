# Sliding Window

## What is it?

The **sliding window** technique keeps a contiguous range of an array or string (the "window") and **moves it along** the input one step at a time. Instead of recomputing everything for each range, you update the answer by adding the element that enters the window and removing the one that leaves.

That turns many O(n·k) or O(n²) problems into O(n).

## When to reach for it

- The question is about a **contiguous** subarray or substring.
- You are asked for the longest, shortest, maximum, minimum, or a count of such ranges.
- A running value (sum, count of vowels, letter frequencies) can be **updated incrementally**.

## The three patterns

### 1. Fixed-size window

The window length `k` never changes. Build the first window, then slide it.

```python
window = sum(nums[:k])
best = window
for i in range(k, len(nums)):
    window += nums[i] - nums[i - k]   # add new, drop old
    best = max(best, window)
```

Used for: maximum average, counting windows above a threshold, maximum vowels.

### 2. Variable-size window

The window **grows** by moving `right`, and **shrinks** by moving `left` whenever a rule is broken (or, for "shortest" problems, whenever the window is good enough).

```python
left = 0
for right in range(len(nums)):
    # add nums[right] to the window state
    while window_is_invalid():
        # remove nums[left] from the window state
        left += 1
    best = max(best, right - left + 1)
```

Used for: shortest subarray with a sum, longest substring without repeats, longest run after replacements.

### 3. Window + frequency map

Track how many times each character appears in the window (a dictionary or `Counter`) and compare it with what you need.

```python
from collections import Counter
need = Counter(t)
window = Counter()
# add/remove characters as the window slides and compare window with need
```

Used for: permutations, anagrams, minimum window containing all characters.

## Complexity

| Pattern | Time | Extra space |
|---|---|---|
| Fixed-size | O(n) | O(1) |
| Variable-size | O(n) | O(1) or O(alphabet) |
| With frequency map | O(n) | O(alphabet) |

Each element is added once and removed at most once, which is why a nested `while` inside the `for` loop is still O(n).

## Common mistakes

- Forgetting to **remove** the outgoing element when the window slides.
- Off-by-one errors in window length: it is `right - left + 1`.
- Updating the answer **before** the window is valid (or after it has already shrunk too far).
- For "shortest window" problems, shrinking only until valid instead of **while** valid.
- Comparing whole `Counter` objects without deleting zero counts, so equal windows look different.

## Problems in this folder

| # | Problem | Pattern |
|---|---------|---------|
| 1 | [Maximum Average Subarray](01_maximum_average_subarray/) | Fixed-size window |
| 2 | [Sub-arrays of Size K With Average At Least Threshold](02_subarrays_average_threshold/) | Fixed-size window |
| 3 | [Maximum Number of Vowels in a Substring](03_max_vowels_in_substring/) | Fixed-size window |
| 4 | [Minimum Size Subarray Sum](04_minimum_size_subarray_sum/) | Variable-size window |
| 5 | [Longest Substring Without Repeating Characters](05_longest_substring_no_repeats/) | Variable-size window |
| 6 | [Longest Repeating Character Replacement](06_longest_repeating_character_replacement/) | Variable-size window |
| 7 | [Permutation in String](07_permutation_in_string/) | Window + frequency map |
| 8 | [Find All Anagrams in a String](08_find_all_anagrams/) | Window + frequency map |
| 9 | [Minimum Window Substring](09_minimum_window_substring/) | Window + frequency map |

Each folder has a `README.md` (question, examples, expected output), a `solution.py` to fill in and a `test.py`.
