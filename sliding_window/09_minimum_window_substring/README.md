# 09. Minimum Window Substring

**Topic:** Sliding Window  |  **Pattern:** Window + frequency map

## Question

Given two strings `s` and `t`, return the shortest substring of `s` that contains every character of `t`, including duplicates.

If no such substring exists, return the empty string `""`. When a valid answer exists, it is guaranteed to be unique.

## Examples

**Example 1**

```
Input:  s = 'ADOBECODEBANC', t = 'ABC'
```

Expected output: `'BANC'`

Explanation: The shortest window containing "A", "B" and "C" is "BANC".

**Example 2**

```
Input:  s = 'a', t = 'a'
```

Expected output: `'a'`

Explanation: The whole string is the window.

**Example 3**

```
Input:  s = 'a', t = 'aa'
```

Expected output: `''`

Explanation: `t` needs two "a"s but `s` has only one, so no window exists.

## Constraints

- `1 <= len(s), len(t) <= 100000`
- Both strings consist of uppercase and lowercase English letters
- If `t` has a letter twice, the window must contain it at least twice

## Your task

Implement `min_window` in [`solution.py`](solution.py).

```python
def min_window(s: str, t: str) -> str:
```

## Hint

Count what you still need. Expand `right` until the window covers `t`, then shrink `left` as far as possible while it still does, recording the best.

## Check your work

```bash
python test.py          # tests your solution.py
(try it yourself first!)
```
