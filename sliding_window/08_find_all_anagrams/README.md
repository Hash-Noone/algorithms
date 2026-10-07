# 08. Find All Anagrams in a String

**Topic:** Sliding Window  |  **Pattern:** Window + frequency map

## Question

Given two strings `s` and `p`, return a list of all start indices in `s` where an anagram of `p` begins.

An anagram is a rearrangement of the same letters. The indices may be returned in any order.

## Examples

**Example 1**

```
Input:  s = 'cbaebabacd', p = 'abc'
```

Expected output: `[0, 6]` (any order)

Explanation: The substring at index 0 is "cba" and the one at index 6 is "bac". Both are anagrams of "abc".

**Example 2**

```
Input:  s = 'abab', p = 'ab'
```

Expected output: `[0, 1, 2]` (any order)

Explanation: The substrings at indices 0, 1 and 2 are "ab", "ba" and "ab".

**Example 3**

```
Input:  s = 'a', p = 'ab'
```

Expected output: `[]` (any order)

Explanation: `p` is longer than `s`, so there can be no anagram.

## Constraints

- `1 <= len(s), len(p) <= 30000`
- Both strings consist of lowercase English letters

## Your task

Implement `find_anagrams` in [`solution.py`](solution.py).

```python
def find_anagrams(s: str, p: str) -> List[int]:
```

## Hint

Same fixed window as the previous problem, but you record every position that matches instead of stopping at the first.

## Check your work

```bash
python test.py          # tests your solution.py
(try it yourself first!)
```
