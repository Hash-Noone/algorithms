# 05. Longest Substring Without Repeating Characters

**Topic:** Sliding Window  |  **Pattern:** Variable-size window

## Question

Given a string `s`, return the length of the longest substring that contains no repeated characters.

## Examples

**Example 1**

```
Input:  s = 'abcabcbb'
```

Expected output: `3`

Explanation: The longest substring without repeats is "abc", length 3.

**Example 2**

```
Input:  s = 'bbbbb'
```

Expected output: `1`

Explanation: Every character is "b", so the best is "b", length 1.

**Example 3**

```
Input:  s = 'pwwkew'
```

Expected output: `3`

Explanation: The answer is "wke", length 3. Note that "pwke" is a subsequence, not a substring.

## Constraints

- `0 <= len(s) <= 50000`
- `s` can contain letters, digits, symbols and spaces

## Your task

Implement `length_of_longest_substring` in [`solution.py`](solution.py).

```python
def length_of_longest_substring(s: str) -> int:
```

## Hint

Keep a set (or a map of last-seen positions). When the new character is already in the window, shrink from the left until it is gone.

## Check your work

```bash
python test.py          # tests your solution.py
(try it yourself first!)
```
