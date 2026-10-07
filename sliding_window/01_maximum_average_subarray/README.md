# 01. Maximum Average Subarray

**Topic:** Sliding Window  |  **Pattern:** Fixed-size window

## Question

Given an integer array `nums` and an integer `k`, find the contiguous subarray of length exactly `k` that has the largest average.

Return that average as a float. Answers within `1e-5` of the true value are accepted.

## Examples

**Example 1**

```
Input:  nums = [1, 12, -5, -6, 50, 3], k = 4
```

Expected output: `12.75`

Explanation: The best window is `[12, -5, -6, 50]` with sum 51, so the average is `51 / 4 = 12.75`.

**Example 2**

```
Input:  nums = [5], k = 1
```

Expected output: `5.0`

Explanation: Only one window exists.

**Example 3**

```
Input:  nums = [-1], k = 1
```

Expected output: `-1.0`

Explanation: Only one window exists.

## Constraints

- `1 <= k <= len(nums) <= 100000`
- `-10000 <= nums[i] <= 10000`

## Your task

Implement `find_max_average` in [`solution.py`](solution.py).

```python
def find_max_average(nums: List[int], k: int) -> float:
```

## Hint

Compute the sum of the first `k` elements, then slide: add the new element, subtract the one that left. Compare sums and divide once at the end.

## Check your work

```bash
python test.py          # tests your solution.py
(try it yourself first!)
```
