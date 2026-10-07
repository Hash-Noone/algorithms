# 03. Container With Most Water

**Topic:** Two Pointers  |  **Pattern:** Opposite-direction pointers

## Question

You are given an array `height` where `height[i]` is the height of a vertical line drawn at position `i`.

Pick two lines. Together with the x-axis they form a container. Return the maximum amount of water a container can hold.

The container cannot be tilted. Its water level is limited by the shorter of the two lines.

## Examples

**Example 1**

```
Input:  height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
```

Expected output: `49`

Explanation: The lines at index 1 (height 8) and index 8 (height 7) are 7 apart: `min(8, 7) * 7 = 49`.

**Example 2**

```
Input:  height = [1, 1]
```

Expected output: `1`

Explanation: Only one container is possible: `min(1, 1) * 1 = 1`.

**Example 3**

```
Input:  height = [4, 3, 2, 1, 4]
```

Expected output: `16`

Explanation: The two lines of height 4 are 4 apart: `4 * 4 = 16`.

## Constraints

- `2 <= len(height) <= 100000`
- `0 <= height[i] <= 10000`

## Your task

Implement `max_area` in [`solution.py`](solution.py).

```python
def max_area(height: List[int]) -> int:
```

## Hint

Start with the widest container. Moving the taller line inward can never help, so move the shorter one.

## Check your work

```bash
python test.py          # tests your solution.py
(try it yourself first!)
```
