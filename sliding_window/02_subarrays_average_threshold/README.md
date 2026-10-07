# 02. Sub-arrays of Size K With Average At Least Threshold

**Topic:** Sliding Window  |  **Pattern:** Fixed-size window

## Question

Given an integer array `arr` and two integers `k` and `threshold`, return how many contiguous sub-arrays of length exactly `k` have an average greater than or equal to `threshold`.

## Examples

**Example 1**

```
Input:  arr = [2, 2, 2, 2, 5, 5, 5, 8], k = 3, threshold = 4
```

Expected output: `3`

Explanation: `[2, 5, 5]`, `[5, 5, 5]` and `[5, 5, 8]` have averages 4, 5 and 6, all at least 4.

**Example 2**

```
Input:  arr = [11, 13, 17, 23, 29, 31, 7, 5, 2, 3], k = 3, threshold = 5
```

Expected output: `6`

Explanation: Six windows of size 3 have an average of at least 5.

**Example 3**

```
Input:  arr = [1], k = 1, threshold = 1
```

Expected output: `1`

Explanation: The single window `[1]` has average 1, which meets the threshold.

## Constraints

- `1 <= k <= len(arr) <= 100000`
- `1 <= arr[i] <= 10000`
- `0 <= threshold <= 10000`

## Your task

Implement `count_subarrays` in [`solution.py`](solution.py).

```python
def count_subarrays(arr: List[int], k: int, threshold: int) -> int:
```

## Hint

Compare the window sum with `k * threshold` instead of computing averages. That avoids floats entirely.

## Check your work

```bash
python test.py          # tests your solution.py
(try it yourself first!)
```
