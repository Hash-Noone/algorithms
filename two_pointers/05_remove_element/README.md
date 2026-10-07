# 05. Remove Element

**Topic:** Two Pointers  |  **Pattern:** Same-direction (slow & fast) pointers

## Question

Given an array `nums` and a value `val`, remove every occurrence of `val` **in place**.

Return `k`, the number of elements that are not equal to `val`. The first `k` positions of `nums` must hold those elements (their order may change). What is stored after position `k` does not matter.

## Examples

**Example 1**

```
Input:  nums = [3, 2, 2, 3], val = 3
```

Expected output: `k = 2`, and `nums[:k]` holds `[2, 2]` (any order)

Explanation: Two elements are not 3, so `k = 2` and the first two slots hold `[2, 2]`.

**Example 2**

```
Input:  nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
```

Expected output: `k = 5`, and `nums[:k]` holds `[0, 1, 3, 0, 4]` (any order)

Explanation: Five elements are not 2, so `k = 5`. The kept values can be in any order.

**Example 3**

```
Input:  nums = [1, 2, 3], val = 4
```

Expected output: `k = 3`, and `nums[:k]` holds `[1, 2, 3]` (any order)

Explanation: `4` is not in the array, so nothing is removed and `k = 3`.

## Constraints

- `0 <= len(nums) <= 100`
- Modify `nums` in place
- O(1) extra space

## Your task

Implement `remove_element` in [`solution.py`](solution.py).

```python
def remove_element(nums: List[int], val: int) -> int:
```

## Hint

Same idea as the previous problem: `fast` reads every element, `slow` writes the ones you keep.

## Check your work

```bash
python test.py          # tests your solution.py
(try it yourself first!)
```
