# 08. 3Sum Closest

**Topic:** Two Pointers  |  **Pattern:** Two pointers + sorting

## Question

Given an integer array `nums` and an integer `target`, choose three different elements whose sum is as close as possible to `target`.

Return that sum (not the elements). Each input has exactly one answer.

## Examples

**Example 1**

```
Input:  nums = [-1, 2, 1, -4], target = 1
```

Expected output: `2`

Explanation: `-1 + 2 + 1 = 2` is the sum closest to 1.

**Example 2**

```
Input:  nums = [0, 0, 0], target = 1
```

Expected output: `0`

Explanation: The only possible sum is 0.

**Example 3**

```
Input:  nums = [1, 1, 1, 0], target = -100
```

Expected output: `2`

Explanation: Every sum is far above -100; the smallest possible sum is `1 + 1 + 0 = 2`.

## Constraints

- `3 <= len(nums) <= 500`
- `-1000 <= nums[i] <= 1000`
- `-10000 <= target <= 10000`

## Your task

Implement `three_sum_closest` in [`solution.py`](solution.py).

```python
def three_sum_closest(nums: List[int], target: int) -> int:
```

## Hint

Same setup as 3Sum: sort, fix one number, move two pointers. Track the sum with the smallest `abs(sum - target)`.

## Check your work

```bash
python test.py          # tests your solution.py
(try it yourself first!)
```
