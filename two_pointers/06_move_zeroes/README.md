# 06. Move Zeroes

**Topic:** Two Pointers  |  **Pattern:** Same-direction (slow & fast) pointers

## Question

Given an array `nums`, move every `0` to the end of the array while keeping the relative order of the non-zero elements.

Do this **in place**. The function returns nothing; it modifies `nums` directly.

## Examples

**Example 1**

```
Input:  nums = [0, 1, 0, 3, 12]
```

Expected output: `nums` becomes `[1, 3, 12, 0, 0]` (the function returns `None`)

Explanation: The non-zeros `1, 3, 12` keep their order and the two zeros go to the end.

**Example 2**

```
Input:  nums = [0]
```

Expected output: `nums` becomes `[0]` (the function returns `None`)

Explanation: A single zero has nowhere to go.

**Example 3**

```
Input:  nums = [1, 2, 3]
```

Expected output: `nums` becomes `[1, 2, 3]` (the function returns `None`)

Explanation: There are no zeros, so nothing changes.

## Constraints

- `0 <= len(nums) <= 10000`
- Modify `nums` in place, do not create a copy of the array

## Your task

Implement `move_zeroes` in [`solution.py`](solution.py).

```python
def move_zeroes(nums: List[int]) -> None:
```

## Hint

`slow` is the position where the next non-zero value belongs. Swap it with `fast` whenever `fast` finds a non-zero.

## Check your work

```bash
python test.py          # tests your solution.py
(try it yourself first!)
```
