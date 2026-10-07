# 04. Minimum Size Subarray Sum

**Topic:** Sliding Window  |  **Pattern:** Variable-size window

## Question

Given an array of **positive** integers `nums` and a positive integer `target`, return the minimal length of a contiguous subarray whose sum is greater than or equal to `target`.

If no such subarray exists, return `0`.

## Examples

**Example 1**

```
Input:  target = 7, nums = [2, 3, 1, 2, 4, 3]
```

Expected output: `2`

Explanation: The subarray `[4, 3]` has sum 7 and length 2. No single element reaches 7.

**Example 2**

```
Input:  target = 4, nums = [1, 4, 4]
```

Expected output: `1`

Explanation: The single element `[4]` already reaches the target.

**Example 3**

```
Input:  target = 11, nums = [1, 1, 1, 1, 1, 1, 1, 1]
```

Expected output: `0`

Explanation: The total of the whole array is 8, which is less than 11, so the answer is 0.

## Constraints

- `1 <= target <= 1000000000`
- `1 <= len(nums) <= 100000`
- `1 <= nums[i] <= 10000`

## Your task

Implement `min_sub_array_len` in [`solution.py`](solution.py).

```python
def min_sub_array_len(target: int, nums: List[int]) -> int:
```

## Hint

Expand `right` and add to the sum. While the sum is big enough, record the length and shrink from `left`.

## Check your work

```bash
python test.py          # tests your solution.py
(try it yourself first!)
```
