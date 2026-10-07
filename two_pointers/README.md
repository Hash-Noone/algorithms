# Two Pointers

## What is it?

The **two pointers** technique uses two index variables that move through an array (or string) so that you can answer a question in a **single pass**, usually O(n) instead of the O(n²) you get from checking every pair.

It works best on **sorted data**, or when you are rearranging or filtering an array **in place**.

## When to reach for it

- You need to find a **pair** (or triple) that meets a condition, and the array is sorted (or can be sorted).
- You need to compare elements from **both ends** of a sequence (palindromes, containers).
- You need to **remove or move** elements in place without extra memory.

## The three patterns

### 1. Opposite-direction pointers

One pointer starts at the left end, the other at the right end. They move toward each other. At each step the current values tell you which pointer to move.

```python
l, r = 0, len(nums) - 1
while l < r:
    # look at nums[l] and nums[r]
    if need_bigger:
        l += 1
    else:
        r -= 1
```

Used for: palindromes, pair sums on sorted arrays, "best pair" problems.

### 2. Same-direction pointers (slow and fast)

Both pointers start on the left and move right. `fast` scans every element. `slow` marks where the next "kept" element should be written.

```python
slow = 0
for fast in range(len(nums)):
    if keep(nums[fast]):
        nums[slow] = nums[fast]
        slow += 1
# nums[:slow] now holds the kept elements
```

Used for: removing duplicates, removing a value, moving zeroes.

### 3. Sort first, then two pointers

Sorting makes the opposite-direction pattern possible. Fix one (or two) elements with a loop, then run two pointers over the rest.

```python
nums.sort()
for i in range(len(nums) - 2):
    l, r = i + 1, len(nums) - 1
    while l < r:
        ...
```

Used for: 3Sum, 3Sum Closest, 4Sum.

## Complexity

| Pattern | Time | Extra space |
|---|---|---|
| Opposite / slow-fast | O(n) | O(1) |
| Sort + two pointers (k-sum) | O(n log n + n^(k-1)) | O(1) beyond the sort |

## Common mistakes

- Using `l <= r` when you need `l < r` (a pointer pairing with itself).
- Forgetting to **skip duplicates** in k-sum problems, which produces repeated answers.
- Moving the wrong pointer. Always ask: "which move can possibly improve the answer?"
- Forgetting that opposite-direction pointers on sums need the array to be **sorted**.

## Problems in this folder

| # | Problem | Pattern |
|---|---------|---------|
| 1 | [Valid Palindrome](01_valid_palindrome/) | Opposite-direction pointers |
| 2 | [Two Sum (Sorted Array)](02_two_sum_sorted/) | Opposite-direction pointers |
| 3 | [Container With Most Water](03_container_with_most_water/) | Opposite-direction pointers |
| 4 | [Remove Duplicates from Sorted Array](04_remove_duplicates_sorted/) | Same-direction (slow & fast) pointers |
| 5 | [Remove Element](05_remove_element/) | Same-direction (slow & fast) pointers |
| 6 | [Move Zeroes](06_move_zeroes/) | Same-direction (slow & fast) pointers |
| 7 | [3Sum](07_three_sum/) | Two pointers + sorting |
| 8 | [3Sum Closest](08_three_sum_closest/) | Two pointers + sorting |
| 9 | [4Sum](09_four_sum/) | Two pointers + sorting |

Each folder has a `README.md` (question, examples, expected output), a `solution.py` to fill in, and a `test.py`.
