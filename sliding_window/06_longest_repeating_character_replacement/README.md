# 06. Longest Repeating Character Replacement

**Topic:** Sliding Window  |  **Pattern:** Variable-size window

## Question

You are given a string `s` of uppercase English letters and an integer `k`. You may change at most `k` characters in `s` to any other uppercase letter.

Return the length of the longest substring that can be made of one repeating letter using at most `k` changes.

## Examples

**Example 1**

```
Input:  s = 'ABAB', k = 2
```

Expected output: `4`

Explanation: Change the two "A"s to "B" (or the two "B"s to "A") to get "BBBB".

**Example 2**

```
Input:  s = 'AABABBA', k = 1
```

Expected output: `4`

Explanation: Change one "A" in "AABA" to "B" to get "AABBBBA", whose longest run of one letter is 4.

**Example 3**

```
Input:  s = 'A', k = 0
```

Expected output: `1`

Explanation: A single character is already a run of length 1.

## Constraints

- `1 <= len(s) <= 100000`
- `s` consists of uppercase English letters
- `0 <= k <= len(s)`

## Your task

Implement `character_replacement` in [`solution.py`](solution.py).

```python
def character_replacement(s: str, k: int) -> int:
```

## Hint

A window is valid if `window_size - count_of_most_common_letter <= k`. Track letter counts inside the window.

## Check your work

```bash
python test.py          # tests your solution.py
(try it yourself first!)
```
