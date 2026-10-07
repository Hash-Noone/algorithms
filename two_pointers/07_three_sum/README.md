# 07. 3Sum

**Topic:** Two Pointers  |  **Pattern:** Two pointers + sorting

## Question

Given an integer array `nums`, return all triplets `[nums[i], nums[j], nums[k]]` where `i`, `j` and `k` are all different and the three numbers add up to `0`.

The answer must not contain duplicate triplets. The order of the triplets, and the order of numbers inside a triplet, does not matter.

## Examples

**Example 1**

```
Input:  nums = [-1, 0, 1, 2, -1, -4]
```

Expected output: `[[-1, -1, 2], [-1, 0, 1]]` (any order)

Explanation: `-1 + 0 + 1 = 0` and `-1 + -1 + 2 = 0`. The triplet `[-1, 0, 1]` appears only once even though `-1` is in the array twice.

**Example 2**

```
Input:  nums = [0, 1, 1]
```

Expected output: `[]` (any order)

Explanation: No three numbers add up to 0.

**Example 3**

```
Input:  nums = [0, 0, 0]
```

Expected output: `[[0, 0, 0]]` (any order)

Explanation: The only triplet is `[0, 0, 0]`.

## Constraints

- `0 <= len(nums) <= 3000`
- `-100000 <= nums[i] <= 100000`

## Your task

Implement `three_sum` in [`solution.py`](solution.py).

```python
def three_sum(nums: List[int]) -> List[List[int]]:
```

## Hint

Sort first. Fix one number, then use two pointers on the rest. Skip repeated values so you never emit the same triplet twice.

## Check your work

```bash
python test.py          # tests your solution.py
(try it yourself first!)
```
