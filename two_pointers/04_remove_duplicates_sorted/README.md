# 04. Remove Duplicates from Sorted Array

**Topic:** Two Pointers  |  **Pattern:** Same-direction (slow & fast) pointers

## Question

Given a sorted array `nums`, remove the duplicates **in place** so that each unique value appears only once. Keep the original relative order.

Return `k`, the number of unique values. The first `k` positions of `nums` must hold the unique values in order. What is stored after position `k` does not matter.

You must use O(1) extra space.

## Examples

**Example 1**

```
Input:  nums = [1, 1, 2]
```

Expected output: `k = 2`, and `nums[:k] = [1, 2]`

Explanation: There are 2 unique values, so `k = 2` and the first two slots are `[1, 2]`.

**Example 2**

```
Input:  nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
```

Expected output: `k = 5`, and `nums[:k] = [0, 1, 2, 3, 4]`

Explanation: There are 5 unique values, so `k = 5`.

**Example 3**

```
Input:  nums = [1, 2, 3]
```

Expected output: `k = 3`, and `nums[:k] = [1, 2, 3]`

Explanation: Nothing to remove, so `k = 3`.

## Constraints

- `0 <= len(nums) <= 30000`
- `nums` is sorted in non-decreasing order
- Modify `nums` in place

## Your task

Implement `remove_duplicates` in [`solution.py`](solution.py).

```python
def remove_duplicates(nums: List[int]) -> int:
```

## Hint

`fast` scans the array. `slow` marks where the next unique value should be written.

## Check your work

```bash
python test.py          # tests your solution.py
(try it yourself first!)
```
