# 09. 4Sum

**Topic:** Two Pointers  |  **Pattern:** Two pointers + sorting

## Question

Given an integer array `nums` and an integer `target`, return all unique quadruplets `[a, b, c, d]` made of four different elements whose sum equals `target`.

The answer must not contain duplicate quadruplets. The order of the quadruplets, and the order of numbers inside one, does not matter.

## Examples

**Example 1**

```
Input:  nums = [1, 0, -1, 0, -2, 2], target = 0
```

Expected output: `[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]` (any order)

Explanation: Three different quadruplets add up to 0.

**Example 2**

```
Input:  nums = [2, 2, 2, 2, 2], target = 8
```

Expected output: `[[2, 2, 2, 2]]` (any order)

Explanation: Many index choices exist, but there is only one unique quadruplet: `[2, 2, 2, 2]`.

**Example 3**

```
Input:  nums = [], target = 0
```

Expected output: `[]` (any order)

Explanation: An empty array has no quadruplets.

## Constraints

- `0 <= len(nums) <= 200`
- `-1000000000 <= nums[i] <= 1000000000`
- `-1000000000 <= target <= 1000000000`

## Your task

Implement `four_sum` in [`solution.py`](solution.py).

```python
def four_sum(nums: List[int], target: int) -> List[List[int]]:
```

## Hint

Sort, fix two numbers with nested loops, then run two pointers on the rest. Skip duplicates at every level.

## Check your work

```bash
python test.py          # tests your solution.py
(try it yourself first!)
```
