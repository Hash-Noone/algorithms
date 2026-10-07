# 02. Two Sum (Sorted Array)

**Topic:** Two Pointers  |  **Pattern:** Opposite-direction pointers

## Question

You are given an array `numbers` that is already sorted in non-decreasing order. Find two different elements that add up to `target`.

Return their positions as `[index1, index2]` using **1-based indexing**, with `index1 < index2`.

Exactly one valid pair exists. You must use only constant extra space.

## Examples

**Example 1**

```
Input:  numbers = [2, 7, 11, 15], target = 9
```

Expected output: `[1, 2]`

Explanation: 2 + 7 = 9, so the answer is indices 1 and 2.

**Example 2**

```
Input:  numbers = [2, 3, 4], target = 6
```

Expected output: `[1, 3]`

Explanation: 2 + 4 = 6, so the answer is indices 1 and 3.

**Example 3**

```
Input:  numbers = [-1, 0], target = -1
```

Expected output: `[1, 2]`

Explanation: -1 + 0 = -1, so the answer is indices 1 and 2.

## Constraints

- `2 <= len(numbers) <= 30000`
- `numbers` is sorted in non-decreasing order
- Exactly one solution exists
- You may not use the same element twice

## Your task

Implement `two_sum_sorted` in [`solution.py`](solution.py).

```python
def two_sum_sorted(numbers: List[int], target: int) -> List[int]:
```

## Hint

If the sum of the two ends is too small, move the left pointer right. If it is too big, move the right pointer left.

## Check your work

```bash
python test.py          # tests your solution.py
(try it yourself first!)
```
