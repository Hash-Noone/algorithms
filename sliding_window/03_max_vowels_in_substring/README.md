# 03. Maximum Number of Vowels in a Substring

**Topic:** Sliding Window  |  **Pattern:** Fixed-size window

## Question

Given a string `s` and an integer `k`, return the maximum number of vowel letters (`a`, `e`, `i`, `o`, `u`) found in any substring of `s` with length exactly `k`.

## Examples

**Example 1**

```
Input:  s = 'abciiidef', k = 3
```

Expected output: `3`

Explanation: The substring "iii" has 3 vowels.

**Example 2**

```
Input:  s = 'aeiou', k = 2
```

Expected output: `2`

Explanation: Any substring of length 2 contains 2 vowels.

**Example 3**

```
Input:  s = 'education', k = 3
```

Expected output: `2`

Explanation: Substrings such as "edu", "uca" and "ion" contain 2 vowels. No length-3 substring has more.

## Constraints

- `1 <= k <= len(s) <= 100000`
- `s` consists of lowercase English letters

## Your task

Implement `max_vowels` in [`solution.py`](solution.py).

```python
def max_vowels(s: str, k: int) -> int:
```

## Hint

Keep a running vowel count for the window. When the window moves, add 1 if the new character is a vowel and subtract 1 if the one that left was.

## Check your work

```bash
python test.py          # tests your solution.py
(try it yourself first!)
```
