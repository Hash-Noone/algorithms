# 07. Permutation in String

**Topic:** Sliding Window  |  **Pattern:** Window + frequency map

## Question

Given two strings `s1` and `s2`, return `True` if `s2` contains a permutation of `s1` as a substring, otherwise `False`.

In other words, return `True` if some substring of `s2` uses exactly the same letters, with the same counts, as `s1`.

## Examples

**Example 1**

```
Input:  s1 = 'ab', s2 = 'eidbaooo'
```

Expected output: `True`

Explanation: The substring "ba" in `s2` is a permutation of "ab".

**Example 2**

```
Input:  s1 = 'ab', s2 = 'eidboaoo'
```

Expected output: `False`

Explanation: No substring of length 2 is "ab" or "ba".

**Example 3**

```
Input:  s1 = 'a', s2 = 'a'
```

Expected output: `True`

Explanation: The strings are identical, so `s2` contains a permutation of `s1`.

## Constraints

- `1 <= len(s1), len(s2) <= 10000`
- Both strings consist of lowercase English letters

## Your task

Implement `check_inclusion` in [`solution.py`](solution.py).

```python
def check_inclusion(s1: str, s2: str) -> bool:
```

## Hint

The window is always `len(s1)` wide. Compare its letter counts with the counts of `s1` as it slides.

## Check your work

```bash
python test.py          # tests your solution.py
(try it yourself first!)
```
